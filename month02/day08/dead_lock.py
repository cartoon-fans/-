from threading import Thread, Lock
from time import sleep


class Account:
    def __init__(self, id, balance, lock):
        self.id = id
        self.balance = balance
        self.lock = lock

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


tom = Account("tom", 5000, Lock())
abby = Account("abby", 8000, Lock())


def transfer(from_, to, amount):
    from_.lock.acquire()
    from_.withdraw(amount)
    from_.lock.release()
    sleep(0.1)
    to.lock.acquire()
    to.deposit(amount)
    to.lock.release()


# transfer(tom, abby, 2000)
t1 = Thread(target=transfer, args=(tom, abby, 2000))
t2 = Thread(target=transfer, args=(abby, tom, 3000))
t1.start()
t2.start()
t1.join()
t2.join()
print(tom.balance)
print(abby.balance)
