class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grades, courses_attached):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя:  {self.name} Фамилия:  {self.surname} Средняя оценка за домашнее задание:  {self.grades} ' \
              f'Завершённые курсы:  {self.finished_courses}'
        return res
    def __lt__(self, other):
        if self < other:
            return other
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname, lec_grades):
        self.name = name
        self.surname = surname
        self.lec_grades = lec_grades

    def __str__(self):
        res = f'Имя:  {self.name} Фамилия:  {self.surname} Средняя оценка за лекцию:  {self.lec_grades}'
        return res

    def __lt__(self, other):
        if self < other:
            return other
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name} Фамилия: {self.surname}'
        return res

def middle_hm(student, course):
    for student in Student:
        print(student)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer = Reviewer('Tomas', 'Edison')
some_lecturer = Lecturer('Some', ' Buddy', 9.7)
best_lecturer = Lecturer('Isaak', 'Newton', 9.9)
some_student = Student('Ruony', 'Eman', 9.6)
best_student = Student('Wiliam', 'Gates', 9.8)

#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
print(some_reviewer)
print(some_lecturer)
print(some_student)
print(best_student.grades)
