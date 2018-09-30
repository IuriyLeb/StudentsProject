# coding: utf8
"""Selection of a random student for answer"""
import random
import RandomStudent

L=100
weight_changed={}

def call_random_student_on_weight(student_dict,flag=1):
	"""
	Selection of random_student considering current weights
	Model of a comparison of the length of the segment of the probability to be answered
	Initially, every student get segment of length 10. After student's answer length of segment will be cut in half
	The boundaries of all segments are shifted
	input data: 1) dictionary of student like {1:name1,2:name2,...} 
				2) dictionary of weights like {1:[0,10],[10:20],...}
	output: return name of student in console
	"""
	if flag==1:
		actual_student_dict = {}
		global actual_student_dict
		student_dict=RandomStudent.check_student_list(student_dict)
	weight={i+1:[L*i,L*(i+1)] for i in range(0,len(student_dict))}

	user_input=raw_input("Press enter for working or q for exit..."+"\n")
	while user_input!="q":
		flag=0
		random_number=random.randint(2,weight[len(student_dict)][1])
		for key in weight:
			if weight[key][0]<=random_number<weight[key][1]:
				print student_dict[key]
				flag=1
				weight[key][1]-=weight_changed.get(key,L)/2
				weight_changed[key]=weight[key][1]-weight[key][0]
				continue
			if flag==1:
				weight[key][0]=weight[key-1][1]
				weight[key][1]=weight[key][0]+weight_changed.get(key,L)

		user_input=raw_input("Press q for exit..."+"\n" +"No if student isn't here" +"\n")
		if user_input=="No":
			del student_dict[key]
			del weight[key]
			actual_student_dict={ind:student_dict[i] for ind,i in enumerate(sorted(student_dict.keys()),1)}
			actual_weight={ind:weight[i] for ind,i in enumerate(sorted(weight.keys()),1)}
			flag=0
			break
	if flag==0:	
		call_random_student_on_weight(actual_student_dict,flag)

if __name__ == '__main__':
	call_random_student_on_weight(student_dict)