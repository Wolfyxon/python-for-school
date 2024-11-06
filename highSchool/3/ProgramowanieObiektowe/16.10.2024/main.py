baza_kontaktow = {
    # name: number
}

class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

def get_contact(query: str) -> Contact:
    for (name, num) in baza_kontaktow.items():
        if name.lower() == query.lower():
            return Contact(name, num)

class Option:
    def __init__(self, display: str):
        self.display = display

    def handler(self):
        raise NotImplementedError()

class New(Option):
    def handler(self):
        name = input("Podaj imię nowego kontaktu: ")
        num = input("Podaj numer telefonu: ")

        if get_contact(name):
            return print("Kontakt już istnieje")

        baza_kontaktow[name] = num
        print("Kontakt dodany!")

class Search(Option):
    def handler(self):
        contact = get_contact(input("Podaj nazwę kontaktu do wyszukania: "))

        if contact:
            print("Numer telefonu:", contact.number)
        else:
            print("Nie znaleziono kontaktu")

class Update(Option):
    def handler(self):
        contact = get_contact(input("Podaj nazwę kontaktu: "))

        if not contact:
            return print("Kontakt nie istnieje")

        num = input("Podaj nowy numer telefonu: ")

        baza_kontaktow[contact.name] = num
        print("Kontakt zaktualizowany!")

class Delete(Option):
    def handler(self):
        contact = get_contact(input("Podaj nazwę kontaktu do usunięcia: "))

        if not contact:
            return print("Kontakt nie istnieje")

        del baza_kontaktow[contact.name]
        print("Kontakt usunięty!")

class Exit(Option):
    def handler(self):
        print("żegnaj")
        exit()

options = [
    New("Dodaj nowy kontakt"),
    Search("Wyszukaj kontakt"),
    Update("Zaktualizuj numer telefonu"),
    Delete("Usuń kontakt"),
    Exit("Zakończ program")
]

def main():
    for i in range(len(options)):
        print(f"{i + 1}. {options[i].display}")

    try:
        opt_id = int(input("Wybierz opcję: "))

        if opt_id < 1 or opt_id > len(options):
            print("Nieznana opcja")
            return main()

        print()
        options[opt_id - 1].handler()

    except ValueError:
        print("Niepoprawna liczba")

    print()
    main()

main()
