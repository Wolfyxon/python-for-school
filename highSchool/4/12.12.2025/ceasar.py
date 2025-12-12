
class Crypt:
    a_index = ord('a')
    letter_count = ord('z') + 1

    def is_letter(self, ch: chr):
        code = ord(ch)
        
        return code >= self.a_index and code <= self.letter_count

    def offset_letter(self, ch: chr, offset: int) -> chr:
        index = ord(ch) - self.a_index
        max_index = self.letter_count - self.a_index
        new_index = (index + offset) % max_index

        return chr(self.a_index + (new_index % max_index) % max_index)

    def offset_str(self, text: str, offset: int) -> str:
        res = ""
        
        for ch in text.lower():
            if self.is_letter(ch):
                res += self.offset_letter(ch, offset)
            else:
                res += ch

        return res

def run_tests():
    crypt = Crypt()

    assert crypt.offset_str("abc", 3) == "def"
    assert crypt.offset_str("xyz", 3) =="abc"
    assert crypt.offset_str("def", -3) == "abc"
    assert crypt.offset_str("abc", 29) == "def"
    assert crypt.offset_str("ab cd", 2) == "cd ef"

def main():
    text = input("Podaj tekst: ")

    print("Podaj klucz (dodatni: szyfrowanie, ujemny: deszyfrowanie)")
    key = int(input("Klucz: "))

    crypt = Crypt()
    text = crypt.offset_str(text, key)

    if key < 0:
        print("Zaszyfrowany tekst:", text)
    elif key > 0:
        print("Odszyfrowany tekst:", text)
    else:
        print("Klucz równy 0. Tekst nie uległ zmianie")

run_tests()
main()
