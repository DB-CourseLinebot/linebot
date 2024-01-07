from frontend.extensions import db
import datetime

class ClassNotification(db.Model):
    __tablename__ = 'class_notifiacation'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), primary_key=True)
    class_id = db.Column(db.Interger, primary_key=True)
    memo = db.Column(db.String(50), nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now()) 
    
    def __init__(self, line_id, class_id, memo=None):
        self.line_id=line_id
        self.class_id=class_id
        self.memo=memo

class TestNotification(db.Model):
    __tablename__ = 'test_notifiacation'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), nullable=False)
    class_id = db.Column(db.String(50), nullable=False)
    notification_time = db.Column(db.DateTime, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now()) 
    
    def __init__(self, line_id, class_id, date_time): 
        self.line_id=line_id
        self.class_id=class_id
        self.notification_time=date_time
