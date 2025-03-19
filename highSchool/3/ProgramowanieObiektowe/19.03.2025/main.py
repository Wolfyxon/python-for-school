local_balance = 200

class BankLog:
    def __init__(self, type: str, amount: float):
        self.type = type
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.type} {self.amount} zł"

class BankAccount:
    def __init__(self, name: str, surname: str, init_balance: float = 0):
        self.history = []
        self.name = name
        self.surname = surname
        self.balance = init_balance

    def __str__(self) -> str:
        return f"{self.name} {self.surname} [{self.balance} zł]"

    def __add_to_history(self, h: BankLog):
        self.history.append(h)

    def historia(self):
        print("Historia", self)

        for i in self.history:
            print(f"- {i}")

    def depozyt(self, kwota: float) -> bool:
        global local_balance

        if local_balance < kwota:
            print("Za mało środków")
            return False
        
        local_balance -= kwota
        self.balance += kwota
        self.__add_to_history(BankLog("depozyt", kwota))

        return True

    def wyplata(self, kwota: float) -> bool:
        global local_balance

        if self.balance < kwota:
            print("Za mało środków na koncie")
            return False
        
        local_balance += kwota
        self.balance -= kwota
        self.__add_to_history(BankLog("wypłata", kwota))

        return True

acc = BankAccount("Sussus", "Amongus", 100)

acc.depozyt(10)
acc.wyplata(20)
acc.wyplata(999999999)
acc.historia()