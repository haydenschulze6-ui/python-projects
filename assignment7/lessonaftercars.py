class Account:
    def __init__(self, pin):
        self.__pin = pin

    def set_pin(self, new_pin):
        self.__pin = new_pin

    def check_pin(self, pin):
        return self.__pin == pin

    def __str__(self):
        return "Account PIN Safety Checker"

account = Account("1234")

print(account)
print(account.check_pin("1234"))
print(account.check_pin("5678"))

account.set_pin("5678")

print(account.check_pin("5678"))