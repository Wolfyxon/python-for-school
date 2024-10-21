Twoim zadaniem jest stworzenie prostego programu do zarządzania bazą kontaktów przy użyciu słowników w języku Python. Program powinien umożliwiać dodawanie nowych kontaktów, wyszukiwanie istniejących kontaktów, aktualizowanie informacji oraz usuwanie kontaktów.

Instrukcje:
1. Stwórz pusty słownik o nazwie "baza_kontaktow".
2. Napisz pętlę, która będzie działać, dopóki użytkownik nie zdecyduje się zakończyć programu.
3. Wewnątrz pętli, użytkownik powinien mieć opcje do wyboru:
   a) Dodawanie nowego kontaktu: Program powinien prosić użytkownika o wprowadzenie imienia i numeru telefonu. Te informacje powinny zostać dodane jako para klucz-wartość do słownika "baza_kontaktow".
   b) Wyszukiwanie kontaktu: Użytkownik powinien móc wprowadzić imię, a program powinien sprawdzić, czy taki kontakt istnieje w bazie i wyświetlić związane z nim informacje.
   c) Aktualizacja informacji: Użytkownik powinien mieć możliwość aktualizowania numeru telefonu istniejącego kontaktu. Program powinien odpytać użytkownika o nowy numer i zaktualizować odpowiedni wpis w słowniku.
   d) Usuwanie kontaktu: Użytkownik powinien podać imię kontaktu do usunięcia, a program powinien go usunąć ze słownika.
   e) Zakończenie programu: Użytkownik powinien móc wybrać opcję zakończenia programu, co zakończy działanie pętli.

Wskazówki:
- Do obsługi różnych opcji możesz użyć instrukcji warunkowych (if, elif, else).
- Do wyjścia z pętli, możesz użyć specjalnej wartości, np. "exit" lub "quit".

Przykład interakcji:
```
Witaj w programie do zarządzania kontaktami!

Co chciałbyś zrobić?
1. Dodaj nowy kontakt
2. Wyszukaj kontakt
3. Zaktualizuj numer telefonu
4. Usuń kontakt
5. Zakończ program

Wybierz opcję: 1
Podaj imię nowego kontaktu: Jan
Podaj numer telefonu: 123-456-789
Kontakt dodany!

Co chciałbyś zrobić?
1. Dodaj nowy kontakt
2. Wyszukaj kontakt
3. Zaktualizuj numer telefonu
4. Usuń kontakt
5. Zakończ program

Wybierz opcję: 2
Podaj imię kontaktu do wyszukania: Jan
Numer telefonu: 123-456-789