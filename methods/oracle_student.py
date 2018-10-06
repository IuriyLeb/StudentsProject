from methods.function_with_name_method_1 import name_function_from_method_1


def oracle(path_to_file_of_student, name_method):
    list_of_student= []
    choser = {name_method : name_function_from_method_1(list_of_student)}
    with open(path_to_file_of_student, "rb") as students_file:
        for line in students_file:
            student_name = line.decode("utf-8").strip().split(" ", 1)[1]
        list_of_student.append(student_name)
    choser[name_method]