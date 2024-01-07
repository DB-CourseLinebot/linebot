from frontend.linebotAPI import *
from frontend.extensions import datetime, timedelta, date, time

def add_test_notification_init(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='請輸入考試科目課號')
    )
    
def add_test_notification_class(event):
    messageText = event.message.text
    print(messageText)
    course_info = get_course_info(int(messageText))
    if course_info == None:
        text_msg1 = TextSendMessage(text='查無此課程')
        text_msg2 = TextSendMessage(text='請重新輸入課號')
        line_bot_api.reply_message(
            event.reply_token,
            [text_msg1, text_msg2]
        )
        return
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
                    "type": "datetimepicker",
                    "label": "確認並設定通知時間",
                    "data": "action=confirm_class_test&course_name="+course_info["course_name"]+"&course_id="+course_info["course_id"],
                    "mode": "datetime"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "重新輸入課號",
                    "data": "action=redo_class_test",
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
                    

def add_test_notification_confirm(event, postback_data):
    print(postback_data)
    print(event.postback.params)
    insert_test(postback_data["course_id"], event.postback.params["datetime"], event.source.user_id)
    date_time = event.postback.params["datetime"].replace("T", " ")
    text_msg = TextSendMessage(text=f'已新增考試通知:\n'+
                                    f'科目: {postback_data["course_name"]}\n'+
                                    f'通知時間: {date_time}')
    line_bot_api.reply_message(
        event.reply_token,
        [text_msg]
    )
    #import to database
    