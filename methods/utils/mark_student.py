import sys


def mark_student(list_of_student):
    todays_students = []
    print('Anybody here y/n?')
    if input() == 'n':
        print('Yahoooo! Have a good rest!')
        sys.exit()
    while not todays_students:
        print('Mark who is absent or here? print absent/here \
        \n q for exit')
        user_input = input()
        for i in range(len(list_of_student)):
            print(i + 1, list_of_student[i])
        print('Please print number of student')
        try:
            if user_input == 'absent':
                absent_student = [int(i) for i in input().split()]
                if absent_student:
                    numb_todays_students = list(
                        set([i for i in range(1, len(list_of_student) + 1)]) - set(absent_student))
                    for numb in numb_todays_students:
                        todays_students.append(list_of_student[numb - 1])
            elif user_input == 'here':
                numb_todays_students = [int(i) for i in input().split()]
                for numb in numb_todays_students:
                    todays_students.append(list_of_student[numb - 1])
            elif user_input == 'q':
                sys.exit("We need a rest! Goodbye!")
            else:
                print('Try again!')

        except ValueError:
            print('Please enter correct integer number of student')

    return (todays_students)
