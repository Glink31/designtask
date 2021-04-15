from random import randint
class Employee():
    def __init__(self,name,isboss=False):
        self.name = name
        self.complete_chance = randint(75,95)
        self.task = None
        self.points = 0
        self.department = None
        self.isboss = isboss
    def completetask(self):
        if self.task is not None:
            self.task.expire()
            if self.task.counter <= 0:
                if randint(1,100) <= self.complete_chance:
                    if self.task.counter == 0:
                        print(f'Сотрудник {self.name} выполнил задание вовремя')
                        self.points +=1
                        self.department.completedtasks +=1
                        self.task = None
                        self.department.notify()
                    elif self.task.counter < 0:
                        print(f'Сотрудник {self.name} выполнил задание не вовремя')
                        self.points -= 1
                        if not self.isboss:
                            self.department.fineboss()
                        self.department.completedtasks +=1
                        self.task = None
                        self.department.notify()
    def assigndepartment(self,department):
        self.department = department