from methods.segments import count_student_weight
from methods.randomizer import check_student_status
from methods.delete_student import delete
from methods.mark_student import delete_absent_student
import sys


def oracle(path_to_file_of_student, name_method, student_array = []):
    list_of_student= []
    choser = {"segments" : count_student_weight,
              "randomizer" : check_student_status,
              "delete" : delete}
    with open(path_to_file_of_student, "rb") as students_file:
        for line in students_file:
            student_name = line.decode("utf-8").strip().split(" ",1)[1]
            list_of_student.append(student_name)
    print('Are all students here? Answer y/n')
    x = input()
    if x == 'n':
        list_of_student = delete_absent_student(list_of_student)
    while True:
        print('Choose a random student? y/n')
        user_input = input()
        if user_input == 'y':
            try:
                student_array = choser[name_method](user_input,list_of_student, student_array)
            except KeyError:
                print("Enter correct name of method \n See help -h, --help")
        elif user_input == 'n':
            sys.exit("Lesson are finished! Good job!")
