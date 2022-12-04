class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_mark(self):
        summary = 0
        if len(self.grades) != 0:
            for key, value in self.grades.items():
                a = sum(value)
                summary += a
            result = summary / len(self.grades)
            return result
        else:
            return 'n/a'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_mark()} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_mark() < lecturer.average_mark()

    def __gt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_mark() > lecturer.average_mark()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_mark(self):
        summary = 0
        if len(self.grades) != 0:
            for key, value in self.grades.items():
                a = sum(value)
                summary += a
                result = summary / len(value)
            return result
        else:
            return 'n/a'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_mark()}'



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_mark_student(student_list, course_name):
    summary_marks = 0
    summary_students = 0
    student: Student
    for student in student_list:
        for course, marks in student.grades.items():
            if course != course_name:
                pass
            else:
                a = sum(marks)
                summary_marks += a
                summary_students += 1
                res = summary_marks/ len(marks) / summary_students
    return f'Средняя оценка студентов по курсу {course_name}: {res}'


def average_mark_lecturers(lecturer_list, course_name):
    summary_marks = 0
    summary_lecturers = 0
    lecturer: Lecturer
    for lecturer in lecturer_list:
        for course, marks in lecturer.grades.items():
            if course != course_name:
                pass
            else:
                a = sum(marks)
                summary_marks += a
                summary_lecturers += 1
                res = summary_marks/ len(marks) / summary_lecturers
                print(summary_lecturers)
    return f'Средняя оценка лекторов по курсу {course_name}: {res}'



student_number1 = Student('Ruoy', 'Eman', 'male')
student_number1.courses_in_progress += ['Java']
student_number1.courses_in_progress += ['Python']

student_number2 = Student('Peter', 'Ivanov', 'male')
student_number2.courses_in_progress += ['Java']
student_number2.courses_in_progress += ['Python']

student_number3 = Student('James', 'Smith', 'male')
student_number3.courses_in_progress += ['Java']

reviewer_number1 = Reviewer('Some', 'Buddy')
reviewer_number1.courses_attached += ['Python']

reviewer_number2 = Reviewer('Some', 'Buddy')
reviewer_number2.courses_attached += ['Java']

lecturer_number1 = Lecturer('Mr', 'Lecturer')
lecturer_number1.courses_attached += ['Python']

lecturer_number2 = Lecturer('Miss', 'Lecturer')
lecturer_number2.courses_attached += ['Java']

reviewer_number1.rate_hw(student_number1, 'Python', 9.5)
reviewer_number1.rate_hw(student_number2, 'Python', 10)

reviewer_number2.rate_hw(student_number1, 'Java', 9)
reviewer_number2.rate_hw(student_number2, 'Java', 7)

student_number1.rate_lecturer(lecturer_number1, 'Python', 9)
student_number1.rate_lecturer(lecturer_number2, 'Java', 8.5)

student_number2.rate_lecturer(lecturer_number1, 'Python', 8.5)
student_number2.rate_lecturer(lecturer_number2, 'Java', 7.5)

student_list = [student_number1, student_number2, student_number3]
lecturer_list = [lecturer_number1, lecturer_number2]

# print(student_number1.grades)
# print(student_number2.grades)
#
# print(lecturer_number1.grades)
# print(lecturer_number2.grades)

# print(student_number1)
# print(reviewer_number1)
# print(lecturer_number1)

# print(lecturer_number2 < student_number1)
# print(lecturer_number2 > student_number1)


# print(average_mark_student(student_list, 'Python'))
#
# print(average_mark_lecturers(lecturer_list, 'Java'))

