from flask import request, jsonify
from model import db, Student, Grade, AverageGrade


def manage_student():
    # Öğrenci ekleme fonksiyonu
    data = request.json
    if 'name' in data and data['name'] != '' and 'surname' in data and data['surname'] != '' and 'stdNumber' in data and \
            data['stdNumber'] != '':
        existing_student = Student.query.filter_by(stdNumber=data['stdNumber']).first()
        if existing_student:
            return jsonify({'message': 'Öğrenci numarası daha önce kayıt edildi.'}), 400
        new_student = Student(name=data['name'], surname=data['surname'], stdNumber=data['stdNumber'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({'message': 'Öğrenci başarıyla eklendi.'}), 201
    else:
        return jsonify({'message': 'İsim, soyisim ve öğrenci numarası zorunlu alan.'}), 400


def add_grade():
    # Course ekleme fonksiyonu
    data = request.json
    if 'course_code' in data and data['course_code'] != '' and 'value' in data  and data['value'] != '' and 'student_id' in data and data['student_id'] != '':
        student = Student.query.get(data['student_id'])
        if not student:
            return jsonify({'message': 'Öğrenci Bulunamadı'}), 404

        existing_grades = Grade.query.filter_by(student_id=data['student_id'], course_code=data['course_code']).all()

        new_grade = Grade(course_code=data['course_code'], value=data['value'], student_id=data['student_id'])
        db.session.add(new_grade)
        db.session.commit()

        if existing_grades:
            average_grade = (sum([grade.value for grade in existing_grades]) + data['value']) / (len(existing_grades) + 1)
            existing_average = AverageGrade.query.filter_by(student_id=data['student_id']).first()
            if existing_average:
                existing_average.grade_average = average_grade
                # Burada yeni notun ID'sini ekliyoruz
                existing_average.grade_id = new_grade.id
            else:
                new_average = AverageGrade(student_id=data['student_id'], grade_average=average_grade, grade_id=new_grade.id)
                db.session.add(new_average)
        else:
            # Yeni not eklendiği için ilk notun ID'sini kullanıyoruz
            new_average = AverageGrade(student_id=data['student_id'], grade_average=data['value'], grade_id=new_grade.id)
            db.session.add(new_average)

        db.session.commit()
        return jsonify({'message': 'Course başarıyla eklendi.'}), 201
    else:
        return jsonify({'message': 'Course code, değer, and öğrenci id zorunlu alan.'}), 400
def get_average_grade(student_id):
    # eklenen course değerlerinin öğreciye göre ortalaması
    students = AverageGrade.query.filter_by(student_id=student_id).group_by(AverageGrade.grade_id).all()
    total_records = AverageGrade.query.count()
    student_name = Student.query.filter_by(id=student_id).first()

    if students:
        student_data = []
        for avg in students:
           course_code = Grade.query.filter_by(id=avg.grade_id).first().course_code
           student_data.append({'course_code': course_code, 'average_grade': avg.grade_average})

        return jsonify({
            'total_records': total_records,
            '.student_name':student_name.name + ' ' + student_name.surname,
            'course_average': student_data
        }), 200
    else:
        return jsonify({'message': 'Derse ilişkin not bulunamadı.'}), 404
