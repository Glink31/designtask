class task():
    def __init__(self,counter):
        self.counter = counter
    def expire(self):
        self.counter -= 1