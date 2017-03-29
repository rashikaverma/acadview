grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

#function to print grades
def print_grades(grades):
    for grade in grades:
        print grade

#function to calculate sum of grades
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

#function to calculate avg of grades
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

#funtion for grade's variance
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        var = (average - score) ** 2
        variance += var
    return variance / len(scores)

#function to return variance
def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)
#calling of above defined functions
print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)




