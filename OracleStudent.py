import argparse
import method 

parser=argparse.ArgumentParser(description='Selection of random student for answer')

group = parser.add_mutually_exclusive_group()
group.add_argument( "-RandomStudent", action="store_true", help='search SNP')
group.add_argument("-segments", action="store_true", help='search indel')
args = parser.parse_args()

list_of_student=open("../data_input/list_of_students.txt").readlines()
student_dict={int(line.strip().split()[0]):line.strip().split("\t",1)[1] for line in list_of_student}

if args.RandomStudent:
	method.RandomStudent.RandomStudents(student_dict)
elif args.segments:
	method.segments.call_random_student_on_weight(student_dict,flag=1)