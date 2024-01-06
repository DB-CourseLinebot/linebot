from extensions import db
import datetime

class ClassNotification(db.Model):
    __tablename__ = 'class_notifiacation'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), primary_key=True)
    class_name = db.Column(db.String(50), primary_key=True)
    class_time = db.Column(db.DateTime, nullable=False)
    class_location = db.Column(db.String(50), nullable=True)
    class_memos = db.Column(db.String(500), nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now()) 
    
    def __init__(self, line_id, class_name, class_time, class_location, class_memos):
        self.line_id=line_id
        self.class_name=class_name
        self.class_time=class_time
        self.class_location=class_location
        self.class_memos=class_memos

class TestNotification(db.Model):
    __tablename__ = 'test_notifiacation'
    id = db.Column(db.Integer, primary_key=True)
    test_time = db.Column(db.DateTime, primary_key=True)
    class_name = db.Column(db.String(50), primary_key=True)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now()) 
    
    def __init__(self, line_id, class_name, class_time, class_location, class_memos): 
        self.line_id=line_id
        self.class_name=class_name
        self.class_time=class_time
