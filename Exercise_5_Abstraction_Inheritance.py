from abc import ABC, abstractmethod


class BankAccount(ABC):
    _balance = 0

    @abstractmethod
    def deposit(self, saadd: int):
        pass

    @abstractmethod
    def withdraw(self, saminus: int):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, add):
        self._balance += add
        print(f'balance after deposit: {self._balance}')

    def withdraw(self, minus):
        if minus > 100:
            print('higher than withdraw limit')
        else:
            self._balance -= minus
            print(f'balance after withdraw: {self._balance}')


class CheckingAccount(BankAccount):
    def deposit(self, add):
        self._balance += 1 - add
        print(f'balance after deposit: {self._balance}')

    def withdraw(self, minus):
        self._balance -= minus
        print(f'balance after withdraw: {self._balance}')


acc1 = SavingsAccount()
acc1.deposit(11)
acc1.withdraw(2)

print("""
    -------
    account 2
""")

acc2 = CheckingAccount()
acc2.deposit(22)
acc2.withdraw(4)


