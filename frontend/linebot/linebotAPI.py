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

line_bot_api = LineBotApi('NVML7/0CX9eZmO0bK8ylIp3A0Dp0QzU3SvrfhbkyyRJQkw1VqHmLbsZ0tYdgB8wKcDdZ0ukyo5ETN3lOiEMxPyLf8kVQjumHt+vbS2dp9sTS8dWXwCM5dVYCeBunovH1gBwswXdnvvrRb7HUvDWf/wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4877833808d769d77908cbd77fa8e29e')