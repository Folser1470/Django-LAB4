groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Соколова",
        "exams": ["Информатика", "АиГ", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Козлов",
        "exams": ["История", "ЭЭиС", "ИС"],
        "marks": [3, 4, 3]
    }
]

def get_average_mark(student):
    marks = student["marks"]
    return sum(marks) / len(marks)

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    print("-" * 80)

    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(15),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20)
        )
    print()

def filter_students_by_average(students, min_average):
    filtered_students = []
    for student in students:
        average = get_average_mark(student)
        if average > min_average:
            filtered_students.append(student)
    return filtered_students

print("Список всех студентов:")
print_students(groupmates)

try:
    min_score = float(input("Введите минимальный средний балл для фильтрации: "))
    filtered = filter_students_by_average(groupmates, min_score)
    if filtered:
        print(f"\nСтуденты со средним баллом выше {min_score}:")
        print_students(filtered)
    else:
        print(f"\nНет студентов со средним баллом выше {min_score}")
except ValueError:
    print("Ошибка: введите корректное число")
