from flask import Flask
from model import db
from routes import manage_student, add_grade, get_average_grade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/nmsri/zyfera_test_case/students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Program çalışmaya başladı.'

@app.route('/students', methods=['POST'])
def manage_student_route():
    return manage_student()


@app.route('/grades', methods=['POST'])
def add_grade_route():
    return add_grade()


@app.route('/average_grade/<student_id>', methods=['GET'])
def get_average_grade_route(student_id):
    return get_average_grade(student_id)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
