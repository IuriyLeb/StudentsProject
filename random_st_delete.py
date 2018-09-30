import random


students = ['Бабкина Ирина', 'Горбач Дарья', 'Кизенко Алена', 'Килина Дарья',
            'Косолапова Анастасия', 'Лебеда Юрий', 'Лебеденко Ольга',
            'Легковой Станислав', 'Лихолетова Дарья', 'Лонишин Любовь',
            'Матвеенко Андрей', 'Матиив Антон', 'Матюхина Наталья', 
            'Моршнева Алиса', 'Намятова Анна', 'Нисканен Сергей', 'Павлова Полина',
            'Погодина Надежда', 'Романова Ольга', 'Рудая Елизавета', 
            'Сытник Екатерина', 'Творогова Варвара', 'Федорова Яна', 
            'Фирулёва Мария', 'Полякова Елена (инф)', 'Балашова Дарья (инф)', 
            'Наталья Зенкова (инф)']
for i in range(len(students)):
  print(i+1, students[i])
print('are all students here? Answer y/n' )
x = input()
if x == 'n':
  print('who is absent today? print their №')
  st_absent = [int(i) for i in input().split()]
  for j in range(1,len(st_absent)+1):
    students.remove(students[j])

while len(students) > 0:
  print('Выбрать случайного студента? y/n' )
  if input() == 'y':
    q = random.choice(students)
    print(q)
    students.remove(q)
