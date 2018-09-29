# кодовое название - массив
# сделать наоборот - вписать присутствующих
# во время цикла чтобы была возможность удалять ушедших
import random


def make_list(dictionary):
    global actual_student_dict
    for i in dictionary:
        student_list.append(dictionary[i])
    return student_list


def revert_dict(dictionary):
    global student_dict_reverted
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
            if elem in actual_student_dict:
                del actual_student_dict[i]
                print('Please continue choosing')
        break


student_list = []
student_dict = {1: 'Бабкина Ирина', 2: 'Горбач Дарья', 3: 'Кизенко Алена',
                4: 'Килина Дарья', 5: 'Косолапова Анастасия', 6: 'Лебеда Юрий',
                7: 'Лебеденко Ольга', 8: 'Легковой Станислав', 9: 'Лихолетова Дарья',
                10: 'Лонишина Любовь', 11: 'Матвеенко Андрей', 12: 'Матиив Антон',
                13: 'Матюхина Наталья', 14: 'Моршнева Алиса', 15: 'Намятова Анна',
                16: 'Нисканен Сергей', 17: 'Павлова Полина', 18: 'Погодина Надежда',
                19: 'Романова Ольга', 20: 'Рудая Елизавета', 21: 'Сытник Екатерина',
                22: 'Федорова Яна', 23: 'Фирулева Мария', }
actual_student_dict = {}
student_dict_reverted = {}
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
                print('Incorrect number')
        print(actual_student_dict)
        break
    else:
        print('Incorrect')
        continue
revert_dict(actual_student_dict)
print('Do you want to make your choise?', '\n', 'Press 1 to do it, 2 to exit')

while True:
    choice2 = input()
    if choice2 == '2':
        break
    elif choice2 == '1':
        somestud = random.choice(make_list(actual_student_dict))
        if student_dict_reverted[somestud] > 0:
            somestud = random.choice(make_list(actual_student_dict))
            student_dict_reverted[somestud] = 0
            print(somestud)
            student_dict_reverted[somestud] += 1
        else:
            print(somestud)
            print(student_dict_reverted[somestud])
            student_dict_reverted[somestud] += 1
            print(student_dict_reverted[somestud])
    elif choice2 == 'gone':
        remove_student()
    else:
        print('Incorrect, try again')
