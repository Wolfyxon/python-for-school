baza_kontaktow = {
    # name: number
}

def get_contact(query: str) -> tuple[str, str]:
    for (name, num) in baza_kontaktow.items():
        if name.lower() == query.lower():
            return name, num

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
        name, num = get_contact(input("Podaj nazwę kontaktu do wyszukania: "))

        if name:
            print("Numer telefonu:", num)
        else:
            print("Nie znaleziono kontaktu")

class Update(Option):
    def handler(self):
        name = input("Podaj nazwę kontaktu: ")

        if not get_contact(name):
            print("Kontakt nie istnieje")
            return

        num = input("Podaj nowy numer telefonu: ")

        baza_kontaktow[name] = num
        print("Kontakt zaktualizowany!")

class Delete(Option):
    def handler(self):
        (name, _num) = get_contact(input("Podaj nazwę kontaktu do usunięcia: "))

        if not name:
            print("Kontakt nie istnieje")
            return

        del baza_kontaktow[name]
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
    print()
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

    main()

main()
