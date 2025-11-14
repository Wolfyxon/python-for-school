import os
import random

max_tries = 10

words = []
remaining_tries = 0
current_word = ""
current_guess = ""

def load_words() -> str:
    global words

    try:
        with open("words.txt", "r", encoding="utf8") as file:
            words = file.read().split("\n")
    except:
        print("Nie można odczytać słownika")
        exit(1)

def reset():
    global remaining_tries, current_guess, current_word

    remaining_tries = max_tries
    current_word = random.choice(words)
    current_guess = "_" * len(current_word)

def play_again():
    if input("Zagrać jeszcze raz? (t/n): ") != "t":
        exit()

    reset()

def win():
    print("Wygrałeś, ale skibidi sigma (masz ohio rizz)!")
    print(f"\"{current_word}\"")

    try:
        with open("wyniki.txt", "a", encoding="utf8") as file:
            file_text = f"Słowo {current_word} | Nieudane próby: {max_tries - remaining_tries}\n"
            file.write(file_text)
    except Exception as e:
        print("Nie można zapisać wyników", e)

    play_again()
    

def lost():
    print("Przegrałeś womp womp!")
    print(f"\"{current_word}\"")
    play_again()

load_words()
reset()

while True:
    print("Pozostałe próby: ", remaining_tries)
    print()
    print(" ".join(list(current_guess)))
    print()

    inp = input("Podaj literę lub słowo: ").lower()
    inp_len = len(inp)

    if inp_len == 0:
        print("Nie podałes nic")
        continue
    if inp_len == 1:
        char = inp[0]
        char_guessed = False

        word_split = list(current_guess)

        for i in range(len(current_word)):
            if current_word[i] == char:
                word_split[i] = char
                char_guessed = True
        
        if not char_guessed:
            print("Nie zgadłeś")
            remaining_tries -= 1
        else:
            current_guess = "".join(word_split)
    else:
        if current_word == inp:
            win()
        else:
            print("Nie zgadłes słowa")
            remaining_tries -= 1

    if current_guess == current_word:
        win()

    if remaining_tries <= 0:
        lost()
