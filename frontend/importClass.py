from frontend.linebotAPI import *
from frontend.sql import *
from frontend.extensions import datetime, timedelta, date, time

def start_import(event):
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='請輸入課號')
    )

def import_course(event):
    messageText = event.message.text
    print(messageText)
    course_info = get_course_info(int(messageText))
    # course_info = get_course_info()
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
                    "data": "action=confirm_class&course_id="+course_info["course_id"],
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
                    "data": "action=redo_class",
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

def confirm_message(event, postback_data):
    course_id = postback_data['course_id']
    return_msg = insert_course(course_id, event.source.user_id)
    if return_msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='確認成功！\n'+f'已將課號{course_id}加入課表')
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='確認失敗！\n'+f'課號{course_id}已在課表中')
        )