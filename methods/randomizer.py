import random


def random_student(list_of_student):
    student_dict = {}
    for elem in list_of_student:
        student_dict[elem] = 0
    # print('Do you want to make your choice?', '\n', 'Press y to do it, n to exit')
    somestud = random.choice(list_of_student)
    print(somestud)
    student_dict[somestud] += 1
    while True:
        print('Proceed? (y/n)', end=' ')
        choice = input()
        if choice == 'n':
            break
        elif choice == 'y':
            somestud = random.choice(list_of_student)
            if student_dict[somestud] > 0:
                somestud = random.choice(list_of_student)
                student_dict[somestud] = 0
            print(somestud)
            student_dict[somestud] += 1
        else:
            print('Incorrect, try again')
