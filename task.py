class Task():
    def __init__(self,department):
        self.department = department
        if self.department == 'Дизайн':
            self.counter = 5
        elif self.department == 'Фронтэнд':
            self.counter = 6
        elif self.department == 'Бэкэнд':
            self.counter = 4
    def expire(self):
        self.counter -= 1