# Создаем класс Account, дальше круглые скобочки и двоеточие:

class Account():

    # Cоздать функцию инициализации (создания), в которой будут находиться все необходимые характеристики. В данном случае это уникальный идентификатор владельца и баланс счета

    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    # Добавляем методы: депозита, то есть пополнения счета и снятия средств.
    # Метод для внесения средств. Прописываем функцию deposit, при использовании которой будет вписываться какая-то сумма money — аргумент функции.

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счете - {self.balance}")

    # Метод для снятия средств:
    def withdraw(self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счёте")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете: {self.balance}")

    # Функция вывода баланса

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")

man = Account("123344555", 600)
man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)

