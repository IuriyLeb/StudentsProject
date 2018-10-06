import argparse
#import method
import os

parser=argparse.ArgumentParser(description='Selection of random student for answer')
group = parser.add_mutually_exclusive_group()
group.add_argument( "--name_method", action="store_true", help='name of random student method')
args = parser.parse_args()

path_to_list_of_student = os.path.join("data_input","list_of_students.txt")
if args.name_method:
    print(1)
    #method.name_method.name_function_from_method(path_to_list_of_student)
