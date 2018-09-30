import random


student_list = []
actual_student_dict = {}
student_dict_reverted = {}
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

def check_student_list(student_dict,flag=1):
    print('Ready to start checking? Y/n')
    global actual_student_dict
    while True:
        choice1 = input()
        if choice1 == 'n':
            return student_dict
            break
        elif choice1 == 'Y':
            for elem in student_dict:
                print(elem, student_dict[elem])
            print('Who is here today?(Type a number)')
            numadd = input().split()
            for ind,elem in enumerate(numadd,1):
                elem = int(elem)
                if elem in student_dict:
                    actual_student_dict[ind] = student_dict[elem]
                else:
                    print('Incorrect number')
            return (actual_student_dict)
            break
        else:
            print('Incorrect')
            continue


def RandomStudents(student_dict):

    check_student_list(student_dict)
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

if __name__ == '__main__':
    list_of_student=open("../data_input/list_of_students.txt").readlines()
    student_dict={int(line.strip().split()[0]):line.strip().split("\t",1)[1] for line in list_of_student}


    RandomStudents()