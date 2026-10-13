from os import name


def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")

def get_student_info():
    name = input("Enter your name:  ")
    score1 = input("Enter your score for assesment 1:  ")
    score2 = input("Enter your score for assesment 2:  ")
    score3 = input("Enter your score for assesment 3:  ")
    return name, score1, score2, score3

def evaluate_performance(score1, score2, score3):
    average = score1 + score2 + score3
    if average < 75:
            print ("Needs Improvement")
    if average >= 75:
            print ("Fairly satisfactory")
    if average >= 80:
            print ("Satisfactory")
    if average >= 85:
            print ("Very satisfactory")
    if average >= 90:
            print ("Outstanding")
    return average

def display_report():
    print ("Student name :", name)

display_header()
get_student_info()
evaluate_performance()
display_report()

