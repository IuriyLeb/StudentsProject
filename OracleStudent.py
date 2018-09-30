import argparse
import method 

parser=argparse.ArgumentParser(description='Selection of random student for answer')

group = parser.add_mutually_exclusive_group()
group.add_argument( "-RandomStudent", action="store_true", help='search SNP')
group.add_argument("-segments", action="store_true", help='search indel')
group.add_argument("-random_st_delete", action="store_true", help='search indel')

args = parser.parse_args()

list_of_student=[line.strip().split("\t",1)[1] for line in open("../data_input/list_of_students.txt").readlines()]
student_dict={ind:student for ind,student in enumerate(list_of_student,1)}



if args.RandomStudent:
	method.RandomStudent.RandomStudents(student_dict)
elif args.segments:
	method.segments.call_random_student_on_weight(student_dict,flag=1)
elif args.random_st_delete:
	method.random_st_delete.random_st_delete(list_of_student)



