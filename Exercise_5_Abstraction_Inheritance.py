from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self):
        self._balance = 0

    @abstractmethod
    def deposit(self, saadd: int):
        pass

    @abstractmethod
    def withdraw(self, saminus: int):
        pass

    @abstractmethod
    def getter(self):
        pass

    @abstractmethod
    def setter(self, new_balance):
        pass


class SavingsAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)

    def deposit(self, add):
        self._balance += add
        print(f'balance after deposit: {self._balance}')

    def withdraw(self, minus):
        if minus > 100:
            print('higher than withdraw limit')
        else:
            self._balance -= minus
            print(f'balance after withdraw: {self._balance}')

    def getter(self):
        print(f'getter balance: {self._balance}')

    def setter(self, new_balance):
        self._balance = new_balance
        print(f"Setter balance change: {self._balance}")


class CheckingAccount(BankAccount):
    def deposit(self, add):
        self._balance += 1 - add
        print(f'balance after deposit: {self._balance}')

    def withdraw(self, minus):
        self._balance -= minus
        print(f'balance after withdraw: {self._balance}')

    def getter(self):
        print(f'getter balance: {self._balance}')

    def setter(self, new_balance):
        self._balance = new_balance
        print(f"Setter balance change: {self._balance}")




acc1 = SavingsAccount()
acc1.deposit(11)
acc1.withdraw(2)
acc1.setter(100)
acc1.getter()

print("""
    -------
    account 2
""")

acc2 = CheckingAccount()
acc2.deposit(22)
acc2.withdraw(4)
acc1.setter(5000)
acc1.getter()
