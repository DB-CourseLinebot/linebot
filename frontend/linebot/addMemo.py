from linebotAPI import *
from url import *
from urllib.parse import parse_qsl
from datetime import datetime, timedelta, date, time
from response import *

def add_class_memo_init(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='請輸入欲修改備註的課號')
    )
    
def add_class_memo_class(event):
    messageText = event.message.text
    print(messageText)
    print('test1')
    # course_info = get_course_info(int(messageText))
    course_info = get_course_info()
    print('test2')
    flex_msg = FlexSendMessage(
        alt_text='確認課程資訊',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "課號",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_id"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "課名",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_name"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "授課教師",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_teacher"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "上課時間",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_time"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "上課地點",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_location"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "備註",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_memo"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    }
                    ]
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "確認",
                    "text": "確認"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "message",
                    "label": "重新輸入課號",
                    "text": "重新輸入課號"
                    }
                }
                ],
                "flex": 0
            }
        }
    )
    print('test3')
    text_msg = TextSendMessage(text='請確認課程資訊')
    line_bot_api.reply_message(
            event.reply_token,
            [text_msg, flex_msg]
    )                 

def add_class_memo_memo(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='請輸入備註')
    )

# def add_test_notification_pre(event, postback_data):
#     print(postback_data)
#     quick_reply_buttons = []
#     test_days = get_test_op()
#     for day in test_days:
#         quick_reply_button = QuickReplyButton(action=PostbackAction(label=f'{day}', text=f'{day}', data=f'action=select_test&day={day}&course_id={course_info["course_id"]}'))
#         quick_reply_buttons.append(quick_reply_button)
#     text_message = TextSendMessage(text='請選擇通知時間',
#                                    quick_reply=QuickReply(items=quick_reply_buttons))
#     line_bot_api.reply_message(
#         event.reply_token,
#         [text_message]
#     )

def add_class_memo_confirm(event):
    messageText = event.message.text
    print(messageText)
    # course_info = get_course_info(int(messageText))
    course_info = get_course_info_memo()
    flex_msg = FlexSendMessage(
        alt_text='確認課程資訊',
        contents={
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "課號",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_id"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "課名",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_name"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "授課教師",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_teacher"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "上課時間",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_time"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "上課地點",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_location"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "備註",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": course_info["course_memo"],
                            "wrap": True,
                            "color": "#000000",
                            "size": "sm",
                            "flex": 5
                        }
                        ]
                    }
                    ]
                }
                ]
            }
        }
    )
    text_msg = TextSendMessage(text='已修改課程備註')
    line_bot_api.reply_message(
            event.reply_token,
            [text_msg, flex_msg]
    )
    #import to database
    