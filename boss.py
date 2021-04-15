from employee import Employee
class Boss(Employee):
    def __init__(self,name,isboss=True):
        super().__init__(name)
    def assigntasks(self):
        if len(self.department.tasklist) > 0:
            for i in range (len(self.department.tasklist)):
                for j in range(len(self.department.employees)):
                    if self.department.employees[j].task is None and len(self.department.tasklist)>0:
                        self.department.employees[j].task = self.department.tasklist[i]
                        del self.department.tasklist[i]
                if self.task is None and len(self.department.tasklist) > 0:
                    self.task = self.department.tasklist[i]
                    del self.department.tasklist[i]
