from frontend.extensions import db


class Class(db.Model):
    __tablename__ = 'class'
    Course_number = db.Column(db.VARCHAR(length=15), autoincrement=False, nullable=False, primary_key=True)
    Course_name = db.Column(db.VARCHAR(length=30), autoincrement=False, nullable=True)
    Permanent_course_number = db.Column(db.VARCHAR(length=15), autoincrement=False, nullable=True)
    Credits = db.Column(db.NUMERIC(precision=5, scale=2), autoincrement=False, nullable=True)
    Teacher = db.Column(db.VARCHAR(length=500), autoincrement=False, nullable=True)

    def __init__(self, Course_number, Course_name,Permanent_course_number, Credits, Teacher, Time1, Place1, Time2, Place2, Time3, Place3, Time4, Place4):
        self.Course_number = Course_number
        self.Course_name = Course_name
        self.Permanent_course_number = Permanent_course_number
        self.Credits = Credits
        self.Teacher = Teacher

class TimePlace(db.Model):
    __tablename__ = 'Time'
    Course_number = db.Column(db.VARCHAR(length=15), autoincrement=False, nullable=False, primary_key=True)
    Time = db.Column(db.VARCHAR(length=50), autoincrement=False, nullable=True, primary_key=True)
    Place = db.Column(db.VARCHAR(length=50), autoincrement=False, nullable=True, primary_key=True)
    def __init__(self, Course_number, Time, Place):
        self.Course_number = Course_number
        self.Time = Time
        self.Place = Place
        
