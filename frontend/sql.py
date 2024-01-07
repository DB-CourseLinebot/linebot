from backend.models.user import User
from backend.models.notification import ClassNotification, TestNotification
from backend.models.classes import Class, TimePlace
from frontend.linebotAPI import *
from frontend.extensions import db, parse_qsl
import psycopg2

def handle_user(profile):
    existUser = User.query.filter(User.line_id == profile.user_id).first()
    if not existUser:
        user = User(profile.user_id, profile.display_name, profile.picture_url)
        db.session.add(user)
        db.session.commit()

def insert_course(course_id, line_id):
    course = Class.query.filter(Class.course_id == course_id).first()
    if not course:
        course = ClassNotification(line_id, course.course_id)
        db.session.add(course)
        db.session.commit()
        return True
    else:
        return False
    
def insert_test(course_id, date_time, line_id):
    test = TestNotification(line_id, course_id, date_time)
    db.session.add(test)
    db.session.commit()

def insert_memo(course_id, memo):
    course = ClassNotification.query.filter(ClassNotification.course_id == course_id).first()
    if course:
        course.memo = memo
        db.session.commit()
        return course
    else:
        return None

def get_course_info(course_id):
    course1 = Class.query.filter(Class.course_id == course_id).first()
    if course1:
        match_courses = TimePlace.query.filter(TimePlace.course_id == course_id).all()
        courses = []
        for match_course in match_courses:
            course = {
                "course_id": course1.course_id,
                "course_name": course1.course_name,
                "course_time": match_course.Time,
                "course_location": match_course.Place,
                "course_memo": course1.memo
            }
            courses.append(course)
        return courses

def notify_class(time):
    for course in TimePlace.query.filter(TimePlace.Time == time).all():
        line_bot_api.push_message(course.line_id, TextSendMessage(text="您有一堂課要上囉！\n" + course.course_id + " " + course.course_name + "\n" + course.Place))

def notify_test(time):
    for test in TestNotification.query.filter(TestNotification.date_time == time).all():
        line_bot_api.push_message(test.line_id, TextSendMessage(text="您有一個考試要考囉！\n" + test.course_id + " " + test.course_name + "\n" + test.date_time))