from flask import Flask, request, abort
from extensions import db, migrate
from models.user import User
from models.notification import ClassNotification, TestNotification
from models.classes import Class
# from sql import *
from linebotAPI import *
from url import *
from addTest import *
from addMemo import *
from importClass import *
from datetime import datetime, timedelta, date, time


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pgadmin:20242024@database-2.cgwkybvu4gbu.us-east-1.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.app = app
db.init_app(app)
migrate.init_app(app, db)

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

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)

@handler.add(FollowEvent)
def handle_follow(event):
    print(event)

status = 0
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    global status
    profile = line_bot_api.get_profile(event.source.user_id)
    messageText = event.message.text
    # 匯入課表
    if messageText == "@匯入課表":
        start_import(event)
        status = 1
    elif messageText.isdigit() and status == 1:
        import_course(event)
    # 新增考試通知
    elif messageText == "@新增考試通知":
        add_test_notification_init(event)
        status = 2
    elif messageText.isdigit() and status == 2:
        add_test_notification_class(event)
    # 課程備註 
    elif messageText == "@課程備註":
        add_class_memo_init(event)
        status = 3
    elif messageText.isdigit() and status == 3:
        add_class_memo_class(event)
    elif status == 30:
        add_class_memo_confirm(event)
        status = 0
    # error event
    elif not is_date_format(messageText):
        print(event)
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='請輸入正確指令')
        )
    
@handler.add(PostbackEvent)
def handle_postback(event):
    global status
    profile = line_bot_api.get_profile(event.source.user_id)
    postback_data = dict(parse_qsl(event.postback.data))
    if postback_data['action'] == 'confirm_class':
        confirm_message(event)
        status = 0
    elif postback_data['action'] == 'redo_class':
        start_import(event)
    # test
    elif postback_data['action'] == 'confirm_class_test':
        add_test_notification_time(event, postback_data)
    elif postback_data['action'] == 'redo_class_test':
        add_test_notification_init(event)  
    elif postback_data['action'] == 'select_test':
        add_test_notification_confirm(event, postback_data)
        status = 0
    # memo
    elif postback_data['action'] == 'confirm_class_memo':
        add_class_memo_memo(event)
        status = 30
    elif postback_data['action'] == 'redo_class_memo':
        add_class_memo_init(event)

if __name__ == "__main__":
    app.run()