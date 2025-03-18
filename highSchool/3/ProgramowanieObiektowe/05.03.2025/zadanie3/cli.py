class Option:
    def __init__(self, name: str, value):
        self.name = name
        self.value = value

class OptionStr(Option):
    def __init__(self, value):
        super().__init__(str(value), value)

def query_option_str(options: list, allow_exit: bool = False, show_list: bool = True):
    opts = []

    for i in options:
        opts.append(OptionStr(i))

    return query_option(opts, allow_exit, show_list)

def query_option(options: list[Option], allow_exit: bool = False, show_list: bool = True):
    ln = len(options)
    
    for i in range(ln):
        print(f"{i + 1}) {options[i].name}")

    if allow_exit:
        print(f"{ln + 1}) Wyjdź")

    selected = input_int("> ")

    if allow_exit and selected == ln + 1:
        return

    if selected > ln or selected == 0:
        print("Niepoprawny wybór")
        return menu(options, allow_exit, False)

    opt = options[selected - 1]

    return opt.value

def menu(options: list[Option], allow_exit: bool = False, show_list: bool = True) -> Option:
    for i in options:
        assert callable(i.value), "All options must contain callable functions"

    value = query_option(options, allow_exit, show_list)

    if value:
        value()

    return value

def input_int(text: str) -> int:
    try:
        return int(input(text))
    except ValueError:
        print("Niepoprawna liczba")
        return input_int(text) 

def input_wait():
    input("\nWciśnij enter by kontynuować...")