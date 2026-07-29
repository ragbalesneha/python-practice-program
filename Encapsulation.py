class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


acc = Account(100)
acc.deposit(50)

print(acc.get_balance())  # Output: 150
# print(acc.__balance)    # AttributeError: direct access hidden