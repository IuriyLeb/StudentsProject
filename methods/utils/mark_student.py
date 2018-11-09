import sys


def mark_student(list_of_student):
    todays_students = []
    print("Anybody here y/n?")
    if input() == "n":
        print("Yahoooo! Have a good rest!")
        sys.exit()
    print('Mark who is absent or here? print absent/here')
    user_input = input()
    for i in range(len(list_of_student)):
        print(i + 1, list_of_student[i])
    print('Please print № of student')
    try:
        if user_input == 'absent':
            absent_student = [int(i) for i in input().split()]
            numb_todays_students = set([i for i in range(1, len(list_of_student) + 1)]) - set(absent_student)
            print(numb_todays_students)
        elif user_input == 'here':
            numb_todays_students = [int(i) for i in input().split()]
        else:
            print("Try again!")
        for numb in numb_todays_students:
            todays_students.append(list_of_student[numb - 1])
        return (todays_students)
    except ValueError:
        print("Please enter correct integer number of student")
        mark_student(list_of_student)
