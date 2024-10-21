baza_kontaktow = {
    # name: number
}

class Option:
  def __init__(self, name: str, display: str):
    self.name = name
    self.display = display

  def handler(self):
    raise NotImplementedError()

class Exit(Option):
    def handler(self):
      print("żegnaj")
      exit()

options = [
    Option("new", "Dodaj nowy kontakt"),
    Option("search", "Wyszukaj kontakt"),
    Option("update", "Zaktualizuj numer telefonu"),
    Option("delete", "Usuń kontakt"),
    Exit("exit", "Zakończ program")
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