from employee import Employee
class Boss(Employee):
    def __init__(self,name):
        super().__init__(name)
        self.employees = []
    def completetask(self):
        super().completetask()
    def getemployees(self,name1,name2,name3,name4): #будет вызываться в начале программы, чтобы создать отдел
        n = []
        n.append(name1)
        n.append(name2)
        n.append(name3)
        n.append(name4)
        for i in range(4):
            self.employees.append(Employee(n[i]))
    def assigntasks(self,tasks):
        for i in range (len(tasks)):
            for j in range (5):
                if j < 4 and (self.employees[j].task is None):
                    self.employees[j].task = tasks[i]
                elif j == 4 and (self.task is None):
                    self.task = tasks[i]
                    del tasks[i]