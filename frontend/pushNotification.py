from flask import Flask, request, abort
from frontend.extensions import db, migrate, datetime, timedelta, date, time
from backend.models.user import User
from backend.models.notification import ClassNotification, TestNotification
from frontend.linebotAPI import *
from frontend.sql import *

def class_notification():
    class_time = ""
    if datetime.datetime.now().weekday() == 1:
        class_time += "M"
    elif datetime.datetime.now().weekday() == 2:
        class_time += "T"
    elif datetime.datetime.now().weekday() == 3:
        class_time += "W"
    elif datetime.datetime.now().weekday() :== 4:
        class_time += "R"
    elif datetime.datetime.now().weekday() == 5:
        class_time += "F"
    elif datetime.datetime.now().weekday() == 6:
        class_time += "S"
    else:
        class_time += "U"
        
    if datetime.time.now() == datetime.time(7, 58):
        class_time += "1"
    elif datetime.time.now() == datetime.time(8, 58):
        class_time += "2"
    elif datetime.time.now() == datetime.time(10, 8):
        class_time += "3"
    elif datetime.time.now() == datetime.time(11, 8):
        class_time += "4"
    elif datetime.time.now() == datetime.time(12, 18):
        class_time += "n"
    elif datetime.time.now() == datetime.time(13, 18):
        class_time += "5"
    elif datetime.time.now() == datetime.time(14, 18):
        class_time += "6"
    elif datetime.time.now() == datetime.time(15, 28):
        class_time += "7"
    elif datetime.time.now() == datetime.time(16, 28):
        class_time += "8"
    elif datetime.time.now() == datetime.time(17, 28):
        class_time += "9"
    elif datetime.time.now() == datetime.time(18, 28):
        class_time += "a"
    elif datetime.time.now() == datetime.time(19, 28):
        class_time += "b"
    elif datetime.time.now() == datetime.time(20, 28):
        class_time += "c"
    elif datetime.time.now() == datetime.time(21, 28):
        class_time += "d"
    
    notify_class(class_time)
    

def test_notification():
    notify_test(datetime.datetime.now())