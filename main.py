from employee import Employee
from task import Task
from boss import Boss
from department import Department
d=[]
e=[]
d.append(Department('Дизайн'))
d.append(Department('Фронтэнд'))
d.append(Department('Бэкэнд'))
e.append(Boss('Марк'))
e.append(Employee('Иван'))
e.append(Employee('Алексей'))
e.append(Employee('Сергей'))
e.append(Boss('Денис'))
e.append(Employee('Ярослав'))
e.append(Employee('Кирилл'))
e.append(Employee('Леонтий'))
e.append(Boss('Данил'))
e.append(Employee('Андрей'))
e.append(Employee('Никита'))
e.append(Employee('Владимир'))
for i in range (12):
    if i < 4:
        e[i].assigndepartment(d[0])
        d[0].addemployee(e[i])
    if i >=4 and i < 8:
        e[i].assigndepartment(d[1])
        d[1].addemployee(e[i])
    if i >= 8:
        e[i].assigndepartment(d[2])
        d[2].addemployee(e[i])
for i in range(3):
    d[i].addboss(e[i*4])
d[0].getnextdepartment(d[1])
d[1].getnextdepartment(d[2])
k=0
while d[2].completedtasks < 10:
    k+=1
    if k <= 10:
        d[0].gettasks(Task(d[0].name))
    for i in range(3):
        d[i].completetask()
maxp = -999
p = None
for i in range(12):
    if e[i].points > maxp:
        maxp = e[i].points
        p = e[i]
if p is not None:
    print(f'Лучший сотрудник {p.name}  {p.points} очков')