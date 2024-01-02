from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)


# todo replace '' with 'your channel access token'
configuration = Configuration(access_token='NVML7/0CX9eZmO0bK8ylIp3A0Dp0QzU3SvrfhbkyyRJQkw1VqHmLbsZ0tYdgB8wKcDdZ0ukyo5ETN3lOiEMxPyLf8kVQjumHt+vbS2dp9sTS8dWXwCM5dVYCeBunovH1gBwswXdnvvrRb7HUvDWf/wdB04t89/1O/w1cDnyilFU=') 
# todo replace '' with 'your channel secret'
handler = WebhookHandler('4877833808d769d77908cbd77fa8e29e')


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


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )

if __name__ == "__main__":
    app.run()