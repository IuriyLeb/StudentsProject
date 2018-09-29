# coding: utf8
"""Selection of a random student for answer"""
import random

L=100
list_of_students=open("./data_input/list_of_students.txt").readlines()
students_dict={int(line.strip().split()[0]):line.strip().split("\t",1)[1] for line in list_of_students}
weight={i+1:[L*i,L*(i+1)] for i in range(0,len(students_dict))}
weight_changed={}

def call_random_student_on_weight(students_dict,weight):
	"""
	Select of random_student considering current weights
	Model of a comparison of the length of the segment of the probability to be answered
	Initially, every student get segment of length 10. After student's answer length of segment will be cut in half
	The boundaries of all segments are shifted
	input data: 1) dictionary of student like {1:name1,2:name2,...} 
				2) dictionary of weights like {1:[0,10],[10:20],...}
	output: return name of student in console
	"""
	while input("Press q for exit..."+"\n")!="q":
		random_number=random.randint(2,weight[len(students_dict)][1])
		flag=0
		for key in weight:
			if weight[key][0]<=random_number<weight[key][1]:
				print students_dict[key]
				if user_input=="No":
					del students_dict[key]
				flag=1
				weight[key][1]-=weight_changed.get(key,L)/2
				weight_changed[key]=weight[key][1]-weight[key][0]
				continue
			if flag==1:
				weight[key][0]=weight[key-1][1]
				weight[key][1]=weight[key][0]+weight_changed.get(key,L)

		user_input=("Press q for exit..."+"\n" +"or No if student isn't here" +"\n")


if __name__ == '__main__':
	call_random_student_on_weight(students_dict,weight)