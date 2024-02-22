from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/nuage'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    submitted_by = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class AttendanceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, nullable=False)
    present = db.Column(db.Boolean, nullable=False)
    submitted_by = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(255), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)  # Add this line
    semester = db.Column(db.String(255), nullable=False)
    class_name = db.Column(db.String(255), nullable=False)
    lecture_hours = db.Column(db.Integer, nullable=False)
    submitted_by = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)



class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(255), nullable=False)
    submitted_by = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    class_name = db.Column(db.String(255), nullable=False)
    submitted_by = db.Column(db.String(255), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

@app.route('/attendance_logs', methods=['GET'])
def get_attendance_logs():
    attendance_logs = AttendanceLog.query.all()
    result = [{'id': log.id, 'student_id': log.student_id, 'course_id': log.course_id,
               'present': log.present, 'submitted_by': log.submitted_by,
               'updated_at': log.updated_at.strftime('%Y-%m-%d %H:%M:%S')} for log in attendance_logs]
    print(result)
    return jsonify(result)

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    result = [{'id': course.id, 'course_name': course.course_name, 'department_id': course.department_id,
               'semester': course.semester, 'class_name': course.class_name,
               'lecture_hours': course.lecture_hours, 'submitted_by': course.submitted_by,
               'updated_at': course.updated_at.strftime('%Y-%m-%d %H:%M:%S')} for course in courses]
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
