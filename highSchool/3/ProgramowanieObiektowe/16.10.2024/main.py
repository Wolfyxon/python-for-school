baza_kontaktow = {
    # name: number
}

class Option:
  def __init__(self, display: str):
    self.display = display

  def handler(self):
    raise NotImplementedError()

class Exit(Option):
    def handler(self):
      print("żegnaj")
      exit()

class New(Option):
  def handler(self):
    name = input("Podaj imię nowego kontaktu: ")
    num = input("Podaj numer telefonu: ")

    if name in baza_kontaktow:
      return print("Kontakt już istnieje")

    baza_kontaktow[name] = num
    print("Kontakt dodany!")

class Delete(Option):
  def handler(self):
    name = input("Podaj nazwę kontaktu do usunięcia: ")

    if not name in baza_kontaktow:
      print("Kontakt nie istnieje")
      return
    
    baza_kontaktow[name] = None

options = [
    New("Dodaj nowy kontakt"),
    Option("Wyszukaj kontakt"),
    Option("Zaktualizuj numer telefonu"),
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

    options[opt_id - 1].handler()

  except ValueError:
    print("Niepoprawna liczba")

  main()

main()