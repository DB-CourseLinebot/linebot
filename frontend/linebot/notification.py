from flask import Flask, request, abort
from extensions import db, migrate
from models.user import User
from models.notifyTime import ClassNotification, TestNotification
from linebotAPI import *
from url import *
from notification import *
from importClass import *
from datetime import datetime, timedelta, date, time

def class_notification():
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    time = datetime.now().time()
    # class_list = ClassNotification.query.filter(ClassNotification.class_time >= today, ClassNotification.class_time < tomorrow).all()
    # print(class_list)
    # for i in class_list:
    #     print(i.class_name)
    #     print(i.class_time)
    #     print(i.class_location)
    #     print(i.class_memos)
    #     print(i.line_id)
    #     line_bot_api.push_message(i.line_id, TextSendMessage(text="您有課程要上囉！\n課程名稱："+i.class_name+"\n上課時間："+i.class_time.strftime("%Y-%m-%d %H:%M:%S")+"\n上課地點："+i.class_location+"\n備註："+i.class_memos))
    

def test_notification():
    # test_list = TestNotification.query.filter(TestNotification.test_time >= today, TestNotification.test_time < tomorrow).all()
    # print(test_list)
    # for i in test_list:
    #     print(i.class_name)
    #     print(i.test_time)
    #     print(i.class_location)
    #     print(i.class_memos)
    #     print(i.line_id)
    #     line_bot_api.push_message(i.line_id, TextSendMessage(text="您有考試要考囉！\n課程名稱："+i.class_name+"\n考試時間："+i.test_time.strftime("%Y-%m-%d %H:%M:%S")+"\n考試地點："+i.class_location+"\n備註："+i.class_memos))