from datetime import date
import datetime

class Transaction:
    def __init__(self, type, status):
        self.date = datetime.datetime.now()
        self.type = type
        self.status = status
        self.details = {}

    def print(self):
        return self.__dict__
