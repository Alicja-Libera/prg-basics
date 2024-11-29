def f(sentence):
    # Sumowanie kodów ASCII wszystkich znaków w zdaniu
    total_sum = sum(ord(char) for char in sentence)
    
    # Sprawdzanie, czy suma jest podzielna przez 3
    return total_sum % 3 == 0

# Testowanie funkcji
print(f("hello world"))  # Oczekiwany wynik: True
print(f("university"))   # Oczekiwany wynik: True
print(f("student"))      # Oczekiwany wynik: False
