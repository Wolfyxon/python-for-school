import random
import re

width = 100
init_w = 4
leaves_height = width - 1

def ansi(code: int) -> str:
    return f"\033[0;{code}m"

def style(s: str, code: int) -> str:
    return ansi(code) + s + ansi(0)

def unstyle(s: str) -> str:
    return re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]', "", s)

def printCen(s: str):
    space = " " * ((width - len(unstyle(s))) // 2)

    print(space + s)

def leaves(w: int = 1, max_w: int = init_w):
    if w > max_w:
        w = 4
        max_w += 5

    if max_w > 20:
        return
    
    row = ""

    for i in range(w):
        if i == max_w // init_w:
            row += "8"
        else:
            if random.randint(0, 8) == 0:
                row += style("O", random.randint(30, 36))
            else:
                row += style("*", 32)

    printCen(row)
    leaves(w + 2, max_w)

def trunk(i: int = 1):
    if i > 2: return

    printCen(style("||", 31))
    trunk(i + 1)

printCen(style("X", 33))
leaves()
trunk()