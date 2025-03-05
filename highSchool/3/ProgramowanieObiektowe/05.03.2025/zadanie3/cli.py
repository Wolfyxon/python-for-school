class Option:
    def __init__(self, name: str):
        self.name = name

    def run():
        raise "Not implemented"

def menu(options: list[Option], allow_exit: bool = False, show_list: bool = True) -> bool:
    ln = len(options)
    
    for i in range(ln):
        print(f"{i + 1}) {options[i].name}")

    if allow_exit:
        print(f"{ln}) Anuluj")

    selected = input_int("> ")

    if allow_exit and selected == ln:
        return False

    if selected > ln or selected == 0:
        print("Niepoprawny wybór")
        return menu(options, allow_exit, False)

    options[selected - 1].run()

    return True

def input_int(text: str) -> int:
    try:
        return int(input(text))
    except ValueError:
        print("Niepoprawna liczba")
        return input_int(text) 
