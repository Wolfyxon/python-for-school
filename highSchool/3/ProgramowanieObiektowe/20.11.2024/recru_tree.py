import random
import re

lines = []

width = 100
init_w = 4
leaves_height = width - 1

def ansi(code: int) -> str:
    return f"\033[0;{code}m"

def style(s: str, code: int) -> str:
    return ansi(code) + s + ansi(0)

def unstyle(s: str) -> str:
    return re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]', "", s)

def addCen(s: str):
    space = " " * ((width - len(unstyle(s))) // 2)

    lines.append(space + s + space)

def leaves(w: int = 1, max_w: int = init_w):
    if w > max_w:
        w = 4
        max_w += 5

    if max_w > 23:
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

    addCen(row)
    leaves(w + 2, max_w)

def trunk(i: int = 1):
    if i > 2: return

    addCen(style("|||", 31))
    trunk(i + 1)

for i in range(4): addCen("")

addCen(style("X", 33))
leaves()
trunk()

for li in range(len(lines)):
    line = list(lines[li])

    for ci in range(len(line)):
        if line[ci] == " " and random.randint(0, li + 1) == 0:
            line[ci] = "."

    print("".join(line))