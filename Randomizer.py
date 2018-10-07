import random


def random(list_of_students):
    student_dict = {}
    for elem in list_of_students:
        student_dict[elem] = 0
    print('Do you want to make your choice?', '\n', 'Press y to do it, n to exit')
    while True:
        choice = input()
        if choice == 'n':
            break
        elif choice == 'y':
            somestud = random.choice(list_of_students)
            if student_dict[somestud] > 0:
                somestud = random.choice(list_of_students)
                student_dict[somestud] = 0
            print(somestud)
            student_dict[somestud] += 1
        else:
            print('Incorrect, try again')
