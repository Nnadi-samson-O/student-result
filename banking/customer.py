import random
from transaction import Transaction


class Customer:
    """
    Create a customer. Ensure to supply name, phone number, gender and date of birth.
    System will generate account number.
    """
    def __init__(self, name, phone_number, gender, date_of_birth, account_number=0, transaction={}, balance=0):
        self.name = name
        self.phone = phone_number
        self.gender = gender
        self.date_of_birth = date_of_birth
        

        if account_number == 0:
            self.account_number = self.generate_account_number()
        else:
            self.account_number = account_number
        #self.account_number = random.randint(3000000000, 3999999999) # generate 10-digit random number 
        self.transaction = transaction
        self.balance = balance

    @staticmethod
    def generate_account_number():
        return random.randint(1000000000, 999999999)

    def send_money(self, account_name, account_number, bank_name, amount):
        """
        This method debits customer balance and sends to account number provided.
        Returns boolean to indicate success or failure of transaction.
        """
        if self.balance > amount:
            new_transaction = Transaction("TRANSFER", "STARTED")
            new_transaction.details = {
                "bank_name": bank_name,
                "account_name": account_name,
                "account_number": account_number,
                "amount": amount
            }
            self.balance -= amount # same as self.balance = self.balance - amount
            self.transaction[new_transaction.date] = new_transaction.type
        

    def buy_airtime(self):
        pass

    def make_payment(self):
        pass

    def deposit_cash(self):
        pass

    def print(self):
        return self.__dict__

