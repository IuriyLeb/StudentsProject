def method_1(list_of_student: list, student_array=None) -> str:
    """
    Choose name random student from list of student

    :param list_of_student
    :param student_array,  need for methods using information from previous call function
    :return: name called student
    """
    called_student = list_of_student[0]
    return called_student, student_array
