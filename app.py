from flask import Flask, request, abort
from frontend.extensions import db, migrate, datetime, timedelta, date, time
from backend.models.user import User
from backend.models.notification import ClassNotification, TestNotification
from backend.models.classes import Class, TimePlace
from frontend.sql import *
from frontend.addTest import *
from frontend.addMemo import *
from frontend.importClass import *


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
handling_class = ""
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    global status, handling_class
    profile = line_bot_api.get_profile(event.source.user_id)
    handle_user(profile)
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
    elif status == 30 and handling_class != "" and handling_class.isdigit():
        add_class_memo_confirm(event, int(handling_class))
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
    global status, handling_class
    profile = line_bot_api.get_profile(event.source.user_id)
    postback_data = dict(parse_qsl(event.postback.data))
    if postback_data['action'] == 'confirm_class':
        confirm_message(event, postback_data)
        status = 0
    elif postback_data['action'] == 'redo_class':
        start_import(event)
    # test
    elif postback_data['action'] == 'confirm_class_test':
        add_test_notification_confirm(event, postback_data)
        status = 0
    elif postback_data['action'] == 'redo_class_test':
        add_test_notification_init(event)  
    
    # memo
    elif postback_data['action'] == 'confirm_class_memo':
        handling_class = add_class_memo_memo(event, postback_data)
        status = 30
    elif postback_data['action'] == 'redo_class_memo':
        add_class_memo_init(event)

if __name__ == "__main__":
    app.run()