import random


def random_st_delete(list_of_student):
    for i in range(len(list_of_student)):
        print(i+1, list_of_student[i])
    print('are all students here? Answer y/n')
    x = input()
    if x == 'n':
        print('who is absent today? print their №')
        absent_student = [int(i) for i in input().split()]
        for j in range(len(absent_student)):          
            list_of_student.remove(list_of_student[j])
    while len(list_of_student) > 0:
        print('Choose a random student? y/n')
        user_input = input()
        if user_input == 'y':
            q = random.choice(list_of_student)
            print(q)
            list_of_student.remove(q)
        if user_input == 'n':
            break
