from frontend.linebotAPI import *
from frontend.sql import *
from frontend.extensions import datetime, timedelta, date, time

def add_class_memo_init(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='請輸入欲修改備註的課號')
    )
    
def add_class_memo_class(event):
    messageText = event.message.text
    print(messageText)
    course_info = get_course_info(int(messageText))
    if len(course_info) == 0:
        text_msg1 = TextSendMessage(text='查無此課程')
        text_msg2 = TextSendMessage(text='請重新輸入課號')
        line_bot_api.reply_message(
            event.reply_token,
            [text_msg1, text_msg2]
        )
        return
    time_loc = ""
    for i in course_info:
        time_loc += i["course_time"]+"-"+i["course_location"]+"\n"
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
                            "text": course_info[0]["course_id"],
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
                            "text": course_info[0]["course_name"],
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
                            "text": course_info[0]["course_teacher"],
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
                            "text": "上課資訊",
                            "color": "#aaaaaa",
                            "size": "sm",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": time_loc,
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
                            "text": course_info[0]["course_memo"],
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
                    "type": "postback",
                    "label": "確認",
                    "data": "action=confirm_class_memo&course_id="+str(course_info[0]["course_id"]),
                    "displayText": "確認"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "重新輸入課號",
                    "data": "action=redo_class_memo",
                    "displayText": "重新輸入課號"
                    }
                }
                ],
                "flex": 0
            }
        }
    )
    text_msg = TextSendMessage(text='請確認課程資訊')
    line_bot_api.reply_message(
            event.reply_token,
            [text_msg, flex_msg]
    )                 

def add_class_memo_memo(event, postback_data):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='請輸入備註')
    )
    return postback_data["course_id"]


def add_class_memo_confirm(event, course_id):
    messageText = event.message.text
    print(messageText)
    course_info = insert_memo(course_id, messageText)
    # course_info = get_course_info_memo()
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
                            "text": course_info[0]["course_name"],
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
                            "text": course_info[0]["course_teacher"],
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
                            "text": course_info[0]["course_time"],
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
    