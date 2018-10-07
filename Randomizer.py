import random


def randomly(list_of_students):
    student_dict_reverted = {}
    for elem in list_of_students:
        student_dict_reverted[elem] = 0
    print('Do you want to make your choice?', '\n', 'Press y to do it, n to exit')
    while True:
        choice2 = input()
        if choice2 == 'n':
            break
        elif choice2 == 'y':
            somestud = random.choice(list_of_students)
            if student_dict_reverted[somestud] > 0:
                somestud = random.choice(list_of_students)
                student_dict_reverted[somestud] = 0
                print(somestud)
                student_dict_reverted[somestud] += 1
            else:
                print(somestud)
                student_dict_reverted[somestud] += 1
        else:
            print('Incorrect, try again')
