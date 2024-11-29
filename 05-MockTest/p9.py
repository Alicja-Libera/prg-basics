
def f(sentence):
    vowels = "aeiouy"  # Zbiór samogłosk (w tym 'y')
    count = 0  # Zmienna do liczenia samogłosk
    for i in sentence:  # Iteracja po każdym znaku w zdaniu
        if i in vowels:  # Sprawdzenie, czy znak jest samogłoską
            count += 1  # Zwiększenie licznika, jeśli jest samogłoską
    return count  # Zwrócenie wyniku

# Testowanie funkcji
print(f("water"))        # Oczekiwany wynik: 2
print(f("hello world"))  # Oczekiwany wynik: 3
