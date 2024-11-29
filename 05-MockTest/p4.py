def f(card_number):
 masked_number=card_number[:2]+'*'*10+card_number[-4:]

 return masked_number



# Przykładowe wywołania
print(f("5290312400019022"))  # Oczekiwany wynik: "52**********9022"

