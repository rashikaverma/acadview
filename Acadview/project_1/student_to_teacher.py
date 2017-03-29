lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]


# Add your function below!
#function to calculate average
def average(numbers):
    total = sum(numbers)
    total = float(total)
    result = total / len(numbers)
    return result

#function to get total avg according to student'marks
def get_average(student):
    homework = average(student["homework"])
    quiz = average(student["quizzes"])
    test = average(student["tests"])
    return 0.1 * homework + 0.3 * quiz + 0.6 * test

#function to return the grade of every student
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#calling the above function
print get_letter_grade(get_average(lloyd))

#function to calculate the average of whole class
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
        return average(results)

#calling above function
print get_class_average(students)
