from flask import Flask, request, abort
from extensions import db, migrate
from models.user import User
from linebotAPI import *
from url import *
from importClass import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dytsou:dyt50u@127.0.0.1:5432/linebotproj'
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
    if messageText == "確認" and step == 2:
        confirm_message(event)
        step = 2
    elif messageText == "@匯入課表":
        start_import(event)
        step = 1
    elif messageText.isdigit() and step == 1:
        import_course(event)
        step = 2
    elif messageText == "重新輸入課號" and step == 2:
        start_import(event)
        step = 1
    else:
        error_event(event)
        step = 0
    


if __name__ == "__main__":
    app.run()