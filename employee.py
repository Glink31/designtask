from random import randint
class Employee():
    def __init__(self,name):
        self.name = name
        self.complete_chance = randint(75,95)
        self.task = None
        self.points = 0
    def completetask(self):
        if (self.task is not None) and (self.task.counter <= 0):
            if randint(1,100) <= self.complete_chance:
                print(f'Сотрудник {self.name} выполнил задание вовремя')
                self.points +=1
            else:
                print(f'Сотрудник {self.name} не выполнил задание вовремя')
                self.points -= 1
