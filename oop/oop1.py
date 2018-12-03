import random
class Bank:
    balance=0

    def __init__(self):
        print('hey homie!welcome')
        self.account_id=random.randint(1000,10000)
        print('niggah ur id is',self.account_id)

    def menu(self):
        user_input=int(input('''how can we help u
        1.display
        2.withdraw
        3.deposit
        4.exit '''))
        if user_input==1:
            self.display()
        elif user_input==2:
            self.withdraw()
        elif user_input==3:
            self.deposit()
        else:
            exit()

    def display(self):
        print('your balnce is',self.balance)
        self.menu()

    def withdraw(self):
        amount=int(input('enter amount to withdraw '))
        self.balance=self.balance-amount
        self.display()
        self.menu()

    def deposit(self):
        amount = int(input('enter amount to deposit '))
        self.balance=self.balance+amount
        self.display()
        self.menu()
sbi=Bank()
sbi.menu()
