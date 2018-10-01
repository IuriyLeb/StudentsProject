import random

list_of_student = []
debug = 0


def make_list(dictionary):
    # global actual_student_dict
    for i in dictionary:
        student_list.append(dictionary[i])
    return student_list


def revert_dict(dictionary):
    # global student_dict_reverted
    for i in dictionary:
        student_dict_reverted[dictionary[i]] = 0
    return student_dict_reverted


def remove_student():
    for student in actual_student_dict:
        print(student, student_dict[student])
    print('Who is absent today?(Type a number)')
    while True:
        remstud = input().split()
        for i in remstud:
            i = int(i)
            if i in actual_student_dict:
                del actual_student_dict[i]
                if debug == 1:
                    print(actual_student_dict)
                print('Please continue choosing', '\n', 'Press y to do it, n to exit')
        break


student_list = []  # List
student_dict = {}
'''{1: 'a', 2: 'b', 3: 'c',
                4: 'd', 5: 'e', 6: 'f',
                7: 'g', 8: 'h', 9: 'i',
                10: 'j', 11: 'k', 12: 'l',
                13: 'm', 14: 'n', 15: 'o',
                16: 'p', 17: 'q', 18: 'r',
                19: 's', 20: 't', 21: 'u',
                22: 'v', 23: 'w', }  # Dicrionary contents all possible students'''
actual_student_dict = {}  # Dictionary
student_dict_reverted = {}  # Dictionary


def checkout():
    print('Ready to start checking? Y/n')
    while True:
        choice1 = input()
        if choice1 == 'n':
            break
        elif choice1 == 'Y':
            for elem in student_dict:
                print(elem, student_dict[elem])
            print('Who is here today?(Type a number)')
            numadd = input().split()
            for elem in numadd:
                elem = int(elem)
                if elem in student_dict:
                    actual_student_dict[elem] = student_dict[elem]
                else:
                    print('Incorrect number', elem)
            if debug == 1:
                print(actual_student_dict)
            break
        else:
            print('Incorrect')
            continue

    revert_dict(actual_student_dict)


def choose():
    print('Do you want to make your choice?', '\n', 'Press y to do it, n to exit')
    while True:
        choice2 = input()
        if choice2 == 'n':
            break
        elif choice2 == 'y':
            somestud = random.choice(make_list(actual_student_dict))
            if student_dict_reverted[somestud] > 0:
                somestud = random.choice(make_list(actual_student_dict))
                student_dict_reverted[somestud] = 0
                print(somestud)
                student_dict_reverted[somestud] += 1
            else:
                print(somestud)
                if debug == 1:
                    print(student_dict_reverted[somestud])
                student_dict_reverted[somestud] += 1
                if debug == 1:
                    print(student_dict_reverted[somestud])
        elif choice2 == 'gone':
            remove_student()
        elif choice2 == 'bugs':
            if debug == 1:
                print(actual_student_dict)
        else:
            print('Incorrect, try again')


if __name__ == '__main__':
    with open('list_of_students.txt', 'r', encoding='utf8') as file:
        for lines in file:
            list_of_student.append(lines)
        student_dict = {int(line.strip().split()[0]): line.strip().split("\t", 1)[1] for line in list_of_student}
    checkout()
    choose()
