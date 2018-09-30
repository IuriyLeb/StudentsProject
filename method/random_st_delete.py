import random

def random_st_delete(list_of_student):
  for i in range(len(list_of_student)):
    print(i+1, list_of_student[i])
  print('are all studentslist   here? Answer y/n' )
  x = input()
  if x == 'n':
    print('who is absent today? print their №')
    st_absent = [int(i) for i in input().split()]
    for j in range(1,len(st_absent)+1):
      list_of_student .remove(lit_of_student[j])
  while len(list_of_student ) > 0:
    print('Choose a random student? y/n' )
    if input() == 'y':
      q=random.choice(list_of_student)
      print q
      list_of_student.remove(q)

if __name__ == '__main__':
  list_of_student=[line.strip().split("\t",1)[1] for line in open("../data_input/list_of_students.txt").readlines()]
  random_st_delete (list_of_student)

  
