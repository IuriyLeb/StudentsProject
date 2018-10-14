def delete_absent_student(list_of_student):
    being_here_student = []
    print('Do you want mark who is absent or who is here today? print absent/here')
    user_input = input()
    for i in range(len(list_of_student)):
        print(i+1, list_of_student[i])
    print('Please print № of student')
    try:
        if user_input == 'absent':
            absent_student = [int(i) for i in input().split()]
            numb_being_here_student = set([i for i in range(1,len(list_of_student)+1)]) - set(absent_student)
            print(numb_being_here_student)
        elif user_input == 'here':
            numb_being_here_student = [int(i) for i in input().split()]
        else:
            print("Try again!")
        for numb in numb_being_here_student:
            being_here_student.append(list_of_student[numb - 1])
        return(being_here_student)
    except ValueError:
        print("Please enter correct integer number of student")
        delete_absent_student(list_of_student)
