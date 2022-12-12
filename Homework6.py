import statistics


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def __count_average_grade(self):
        avg_grade = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 2)
        return avg_grade
        
    def __lt__(self, other_student):
        return self.__count_average_grade() < other_student.__count_average_grade()
    
    def __str__(self):
        output = f'Имя: {self.name}\n\
            Фамилия: {self.surname}\n\
                Средняя оценка за домашние задания: {self.__count_average_grade()}\n\
                    Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n\
                        Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return output

     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}
    
    def __count_average_rate(self):
        avg_rate = round(sum(sum(self.rates.values(), [])) / len(sum(self.rates.values(), [])), 2)
        return avg_rate

    def __lt__(self, other_lecturer):
        return self.__count_average_rate() < other_lecturer.__count_average_rate()

    def __str__(self):
        output = f'Имя: {self.name}\n\
                   Фамилия: {self.surname}\n\
                   Средняя оценка за лекции: {self.__count_average_rate()}\n'
        return output


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return output

oleg_b = Lecturer('Олег', 'Булыгин')
oleg_b.courses_attached += ['Python']

adilet_a = Lecturer('Адилет', 'Асанкожоев')
adilet_a.courses_attached += ['Python']

maria_k = Reviewer('Мария', 'Крашенинникова')
maria_k.courses_attached += ['Python', 'Java']

maria_l = Reviewer('Мария', 'Лопатина')
maria_l.courses_attached += ['Python', 'Java']

vadim_p = Student('Вадим', 'Потехин', 'м')
vadim_p.courses_in_progress += ['Python', 'Java']
vadim_p.add_courses('Менеджмент')

oleg_n = Student('Олег', 'Нагорный', 'м')
oleg_n.courses_in_progress += ['Python']
oleg_n.add_courses('Java')

student_list = [vadim_p, oleg_n]
lecturer_list = [oleg_b, adilet_a]


oleg_n.rate_lecturer(oleg_b, 'Python', 10)
oleg_n.rate_lecturer(oleg_b, 'Python', 8)
oleg_n.rate_lecturer(oleg_b, 'Python', 9)
oleg_n.rate_lecturer(adilet_a, 'Python', 9)
oleg_n.rate_lecturer(adilet_a, 'Python', 8)
oleg_n.rate_lecturer(adilet_a, 'Python', 9)

vadim_p.rate_lecturer(oleg_b, 'Python', 9)
vadim_p.rate_lecturer(oleg_b, 'Python', 10)
vadim_p.rate_lecturer(oleg_b, 'Python', 8)
vadim_p.rate_lecturer(adilet_a, 'Python', 10)
vadim_p.rate_lecturer(adilet_a, 'Python', 8)
vadim_p.rate_lecturer(adilet_a, 'Python', 9)

maria_k.rate_hw(vadim_p, 'Python', 10)
maria_k.rate_hw(vadim_p, 'Python', 10)
maria_k.rate_hw(vadim_p, 'Python', 10)
maria_l.rate_hw(vadim_p, 'Python', 10)
maria_l.rate_hw(vadim_p, 'Python', 2)
maria_l.rate_hw(vadim_p, 'Python', 10)
maria_k.rate_hw(vadim_p, 'Java', 1)

maria_k.rate_hw(oleg_n, 'Python', 9)
maria_k.rate_hw(oleg_n, 'Python', 8)
maria_k.rate_hw(oleg_n, 'Python', 10)
maria_k.rate_hw(oleg_n, 'Python', 10)
maria_l.rate_hw(oleg_n, 'Python', 10)
maria_l.rate_hw(oleg_n, 'Python', 7)
maria_l.rate_hw(oleg_n, 'Python', 9)
maria_l.rate_hw(oleg_n, 'Python', 10)



print(maria_l)
print(maria_k)

print(oleg_b)
print(adilet_a)
if oleg_b > adilet_a:
    print(f'{oleg_b.name} {oleg_b.surname} преподает лучше, чем {adilet_a.name} {adilet_a.surname}\n')
else:
    print(f'{adilet_a.name} {adilet_a.surname} преподает лучше, чем {oleg_b.name} {oleg_b.surname}\n')

print(vadim_p)
print(oleg_n)
if oleg_n > vadim_p:
    print(f'{oleg_n.name} {oleg_n.surname} учится лучше, чем {vadim_p.name} {vadim_p.surname}\n')
else:
    print(f'{vadim_p.name} {vadim_p.surname} учится лучше, чем {oleg_n.name} {oleg_n.surname}\n')


def count_avg_course_grade(course, list=student_list):
    sum_count = 0
    lenght_count = 0
    for student in list:
        if course in student.grades:
            sum_count += sum(student.grades[course])
            lenght_count += len(student.grades[course])
    return f'Средний балл студентов за курс {course}: {round(sum_count / lenght_count, 2)}'

def count_avg_course_grade(course, list=student_list):
    sum_count = 0
    lenght_count = 0
    for student in list:
        if course in student.grades:
            sum_count += sum(student.grades[course])
            lenght_count += len(student.grades[course])
    return f'Средняя оценка студентов за курс {course}: {round(sum_count / lenght_count, 2)}'

def count_avg_course_rate(course, list=lecturer_list):
    sum_count = 0
    lenght_count = 0
    for lecturer in list:
        if course in lecturer.rates:
            sum_count += sum(lecturer.rates[course])
            lenght_count += len(lecturer.rates[course])
    return f'Средняя оценка лекторов за курс {course}: {round(sum_count / lenght_count, 2)}'
    

print(count_avg_course_grade("Python"))
print(count_avg_course_grade("Java"))
print(count_avg_course_rate("Python"))

