class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        """
        Перезагружаем метод __str__ и добавляем подсчёт средней оценки
        """
        all_grades = []
        for c_grades in self.grades.values():
            for grade in c_grades:
                all_grades.append(grade)
        self.average_rating = round((sum(all_grades) / len(all_grades)), 1)
        return (f'Имя:{self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_rating}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершённые курсы:{", ".join(self.finished_courses)}')

    def RateLecturer(self, lecturer, course, grade):
        """
        Выставляем оценку преподавателю
        """
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        """
        Перезагружаем метод __str__ и добавляем подсчёт средней оценки
        """
        all_grades = []
        for c_grades in self.grades.values():
            for grade in c_grades:
                all_grades.append(grade)
        self.average_rating = round((sum(all_grades) / len(all_grades)), 1)
        return (f'Имя: {self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за лекции:{self.average_rating}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """
        Выставляем оценку студенту
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Фамилия:{self.surname}'


def avg_student_grade(student_list, course):
    """
    Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    """
    all_student_grades = []
    for student in student_list:
        if isinstance(student, Student) and course in student.courses_in_progress and course in student.grades.keys():
            for grade in student.grades[course]:
                all_student_grades.append(grade)
    if all_student_grades:
        return round((sum(all_student_grades) / len(all_student_grades)), 1)
    else:
        print(f'Курс {course} не найден')
        return


def avg_lecturer_rate(lecturers_list, course):
    """
    подсчет средней оценки за лекции всех лекторов в рамках курса
    """
    all_lectors_grades = []
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in lecturer.grades.keys():
            for grade in lecturer.grades[course]:
                all_lectors_grades.append(grade)
    if all_lectors_grades:
        return round((sum(all_lectors_grades) / len(all_lectors_grades)), 1)
    else:
        print(f'Курс {course} не найден')
        return


# Создаём по 2 объекта каждого класса и выставляем оценки
student1 = Student(name='Владислав', surname='Минаев', gender='male')
student1.courses_in_progress.append('Java')
student1.courses_in_progress.append('Python')
student1.finished_courses.append('Rust')

student2 = Student(name='Арина', surname='Маркина', gender='female')
student2.courses_in_progress.append('Java')
student2.courses_in_progress.append('Rust')

lecturer1 = Lecturer(name='Владислав', surname='Лебедев')
lecturer1.courses_attached.append('Java')
lecturer1.courses_attached.append('Python')

lecturer2 = Lecturer(name='Василиса', surname='Васильева')
lecturer2.courses_attached.append('Java')
lecturer2.courses_attached.append('Rust')

student1.RateLecturer(lecturer1, 'Java', 3)
student1.RateLecturer(lecturer1, 'Python', 5)

student2.RateLecturer(lecturer1, 'Java', 5)
student2.RateLecturer(lecturer2, 'Rust', 9)

reviewer1 = Reviewer(name='Мария', surname='Наумова')
reviewer1.courses_attached.append('Java')
reviewer1.courses_attached.append('Python')

reviewer1.rate_hw(student1, 'Java', 3)
reviewer1.rate_hw(student1, 'Python', 5)

reviewer1.rate_hw(student2, 'Java', 3)
reviewer1.rate_hw(student2, 'Python', 5)

reviewer2 = Reviewer(name='Григорий', surname='Макаров')
reviewer2.courses_attached.append('Java')
reviewer2.courses_attached.append('Rust')

reviewer2.rate_hw(student1, 'Java', 8)
reviewer2.rate_hw(student2, 'Rust', 9)

# Проверяем перезагрузку метода __str__:
print(student1)
print(lecturer1)
print(reviewer1)

# Сравниваем судентов по средней оценке через оператор сравнения:
if student2.average_rating > student1.average_rating:
    print('Рейтинг студента №2 выше, чем у студента №1')

# Сравниваем лекторов по средней оценке через оператор сравнения:
if lecturer1.average_rating < lecturer2.average_rating:
    print('Рейтинг лектора №1 ниже, чем у лектора №2')

students = [student1, student2]  # Список студентов
avg_student_grade(students, 'Python')  # Считаем среднюю оценку студентов по курсу Python

lecturers = [lecturer1, lecturer2]  # Список преподавателей
avg_lecturer_rate(lecturers, 'Python')  # Считаем среднюю оценку преподавателей по курсу Python
