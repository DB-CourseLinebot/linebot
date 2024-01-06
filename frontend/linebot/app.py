from flask import Flask, request, abort
from extensions import db, migrate
from models.user import User
from models.notifyTime import ClassNotification, TestNotification
from models.sql import *
from linebotAPI import *
from url import *
# from notification import *
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

step = 0
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    global step
    profile = line_bot_api.get_profile(event.source.user_id)
    messageText = event.message.text
    print("$$"+messageText)
    print(messageText.isdigit())
    print(step)
    # 匯入課表
    if messageText == "@匯入課表":
        start_import(event)
        step = 1
    elif messageText.isdigit() and step == 1:
        import_course(event)
        step = 2
    elif messageText == "確認" and step == 2:
        confirm_message(event)
        step = 0
    elif messageText == "重新輸入課號" and step == 2:
        start_import(event)
        step = 1
    # 新增考試通知
    elif messageText == "@新增考試通知":
        add_test_notification_init(event)
        step = 11
    elif messageText.isdigit() and step == 11:
        add_test_notification_class(event)
        step = 12
    elif messageText == "確認" and step == 12:
        add_test_notification_time(event)
        step = 13
    elif messageText == "重新輸入課號" and step == 12:
        add_test_notification_init(event)
        step = 11
    # 課程備註 
    elif messageText == "@課程備註":
        add_class_memo_init(event)
        step = 21
    elif messageText.isdigit() and step == 21:
        add_class_memo_class(event)
        step = 22
    elif messageText == "確認" and step == 22:
        add_class_memo_memo(event)
        step = 23
    elif messageText == "重新輸入課號" and step == 22:
        add_class_memo_init(event)
        step = 21
    elif step == 23:
        add_class_memo_confirm(event)
        step = 24
    elif not is_date_format(messageText):
        error_event(event)
    print(f'###{step}')
    
@handler.add(PostbackEvent)
def handle_postback(event):
    global step
    profile = line_bot_api.get_profile(event.source.user_id)
    postback_data = dict(parse_qsl(event.postback.data))
    print(postback_data)
    if postback_data['action'] == 'select_test':
        add_test_notification_confirm(event, postback_data)
        step = 0
    # elif postback_data['action'] == 'select_time':
    #     if step == 13:
    #         add_test_notification_time(event, postback_data['time'])
    #         step = 13
    #     elif step == 23:
    #         add_class_memo_time(event, postback_data['time'])
    #         step = 23

if __name__ == "__main__":
    app.run()