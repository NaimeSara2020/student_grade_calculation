from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    surname = db.Column(db.String(150),nullable=False)
    stdNumber = db.Column(db.Integer, unique=True)
    grades = db.relationship('Grade',backref='student',lazy=True)
    averages = db.relationship('AverageGrade', backref='student', lazy=True)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(10),nullable=False)
    value = db.Column(db.Float, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'),nullable=False)
    averages = db.relationship('AverageGrade', backref='grade', lazy=True)


class AverageGrade(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    grade_average = db.Column(db.Float, nullable=False)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'), nullable=False)
