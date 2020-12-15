import uuid
from datetime import datetime


class Taxes:
    def __init__(self):
        self.tax = 0.01


class BankAccount:

    def __init__(self, acc_name):
        self.tax = Taxes().tax
        self.acc_name = acc_name
        self.account_id = uuid.uuid4()
        self.balance = 0.0
        self.transactions = []

    def deposit_of_funds(self, amount):
        self.balance += amount - (amount * self.tax)
        self.transactions.append((amount, 'deposit', datetime.now().strftime('%d %m %Y')))

    def withdrawal_of_funds(self, amount):
        self.balance -= amount + (amount * self.tax)
        self.transactions.append((amount, 'withdrawal', datetime.now().strftime('%d %m %Y')))

    def get_balance(self):
        return self.balance


client = BankAccount('Client')
client.deposit_of_funds(1000)
print(client.get_balance())
client.withdrawal_of_funds(200)
print(client.get_balance())
client.withdrawal_of_funds(300)
print(client.get_balance())
print(client.transactions)
