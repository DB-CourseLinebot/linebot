from flask import Flask, request, abort
from frontend.linebotAPI import *
import psycopg2

app = Flask(__name__)

line_bot_api = LineBotApi('nxQSC3TPz7jJfc6ovY49aHbGZALrSEMa8O4nLa6gQYGnHyye4Wu9xnVRWZhfVZlg4y4FDczWsPKY0/ENVEoLyc32WCP9EUS78JUw1JfrHNThXFRVMOFsBTZcZ9yAmVLLKBJqOcGGKiNCtr0S3ry/agdB04t89/1O/w1cDnyilFU=') 
handler = WebhookHandler('d82e96a4b1d3f281eb665c10a579bd30')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    user_message = event.message.text

    # 解析使用者的消息
    tokens = user_message.split()
    command = tokens[0].lower()

    # 使用 SQLite 資料庫
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # 設定考試時間
    if command == "考試時間":
        course_code = tokens[1]
        exam_time = tokens[2]
        
        # 存入資料庫
        cursor.execute("INSERT INTO exams (user_id, course_code, exam_time) VALUES (?, ?, ?)",
                       (user_id, course_code, exam_time))
        conn.commit()

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"已設定考試時間：{exam_time}")
        )

    # 帶物品通知
    elif command == "攜帶物品":
        course_code = tokens[1]
        items_to_bring = " ".join(tokens[2:])
        
        # 存入資料庫
        cursor.execute("INSERT INTO reminders (user_id, course_code, items_to_bring) VALUES (?, ?, ?)",
                       (user_id, course_code, items_to_bring))
        conn.commit()

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"已設定攜帶物品通知：{items_to_bring}")
        )
        conn.close()

if __name__ == "__main__":
    app.run()