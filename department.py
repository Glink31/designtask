from task import Task
class Department():
    def __init__(self,name):
        self.name = name
        self.boss = None
        self.employees = []
        self.tasklist = []
        self.completedtasks = 0
        self.nextdepartment = None
    def addemployee(self,employee):
        self.employees.append(employee)
    def addboss(self,boss):
        self.boss = boss
    def fineboss(self):
        if self.boss is not None:
            self.boss.points -= 1
    def gettasks(self,task):
        self.tasklist.append(task)
    def getnextdepartment(self,department):
        self.nextdepartment = department
    def notify(self):
        if self.nextdepartment is not None:
            self.nextdepartment.gettasks(Task(self.nextdepartment.name))
