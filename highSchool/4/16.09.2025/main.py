# Napisz klasę BankAccount, która:
#
#    posiada atrybuty owner (właściciel konta) i balance (saldo),
#    ma metodę deposit(amount) do wpłacania środków,
#    ma metodę withdraw(amount) do wypłacania środków.
#
# Dodaj , która będzie sprawdzać, czy podczas wypłaty na koncie nie pojawi się ujemne saldo.

cash = 100

class BankAccount:
    def __init__(self, owner: str, init_balance: float = 0):
        self.owner = owner
        self.balance = init_balance

    def deposit(self, amount: float):
        global cash
        assert cash >= amount, "Za mało gotówki"

        cash -= amount
        self.balance += amount

    def withdraw(self, amount: float):
        global cash
        assert self.balance >= amount, "Brak środków"

        cash += amount
        self.balance -= amount  

acc = BankAccount("Saddam Husein")
acc.deposit(50)
acc.withdraw(200)
