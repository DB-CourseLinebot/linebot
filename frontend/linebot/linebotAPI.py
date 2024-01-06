from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    StickerSendMessage,
    ImageSendMessage,
    LocationSendMessage,
    FollowEvent,
    UnfollowEvent,
    TemplateSendMessage, 
    ImageCarouselTemplate, 
    ImageCarouselColumn, 
    PostbackAction,
    PostbackEvent,
    FlexSendMessage,
    QuickReply,
    QuickReplyButton,
    MessageAction,
)

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

from datetime import datetime

def is_date_format(text):
    try:
        # Attempt to parse the text as a date
        datetime.strptime(text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

line_bot_api = LineBotApi('9423gG+CS1Cg1EHZSRO54T0wk9dQh6Ed7jcnfn3Gax9XIPw8v+2JjTTwMDROPYx3uOasjTuhSNFrTRTCY9JrXjAeAaVE2JJyGCysCAbfgGD3DtmVEuQV+9LOUmrdwIuxCDeZGGLoec6X6ymAk4QTlAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('01d2b8a4c631309c7f2d6553aeba0532')