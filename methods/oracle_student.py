from methods.segments import call_random_student_on_weight
from methods.randomizer import random_student
from methods.delete_student import random_st_delete


def oracle(path_to_file_of_student, name_method):
    list_of_student= []
    choser = {"segments" : call_random_student_on_weight,
              "randomizer" : random_student,
              "delete" : random_st_delete}
    with open(path_to_file_of_student, "rb") as students_file:
        for line in students_file:
            student_name = line.decode("utf-8").strip().split(" ",1)[1]
            list_of_student.append(student_name)
    try:
        choser[name_method](list_of_student)
    except KeyError:
        print("Enter correct name of method \n See help -h, --help")