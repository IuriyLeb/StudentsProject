from methods.segments import count_student_weight
from methods.randomizer import check_student_status
from methods.delete_student import delete


def oracle(path_to_file_of_student, name_method):
    list_of_student= []
    choser = {"segments" : count_student_weight,
              "randomizer" : check_student_status,
              "delete" : delete}
    with open(path_to_file_of_student, "rb") as students_file:
        for line in students_file:
            student_name = line.decode("utf-8").strip().split(" ",1)[1]
            list_of_student.append(student_name)

    print('are all students here? Answer y/n')
    x = input()
    if x == 'n':
        delete_absent_student(list_of_student)
    while True:
        print('Choose a random student? y/n')
        user_input = input()
        try:
            choser[name_method](user_input,list_of_student)
        except KeyError:
            print("Enter correct name of method \n See help -h, --help")