decimal_number = 304
binary_string = bin(decimal_number)[2:] # ta nietypowa dwójka usuwa prefiks b- odpowieni pewnie za system bianrny
print(binary_string)

# Aby przekonwertować łańcuch binarny reprezentujący liczbę dziesiętną na liczbę całkowitą w Pythonie, najlepiej użyć funkcji int(), podając dodatkowy argument określający system liczbowy, np. 2 dla liczby binarnej.

# Przykład użycia int() dla liczby binarnej reprezentującej liczbę dziesiętną 304:
# Jeśli łańcuch binarny to "100110000" (reprezentuje dziesiętną 304), można skonwertować go na liczbę dziesiętną tak:

# kod w drugą stronę:
# binary_string = "100110000" 
# decimal_number = int(binary_string, 2)  # Zamiana binarnego ciągu na liczbę dziesiętną
# print(decimal_number)  # Wynik: 304
# Wyjaśnienie
# int(binary_string, 2) interpretuje ciąg znaków jako liczbę binarną i konwertuje ją na liczbę dziesiętną.
# Argument 2 wskazuje, że ciąg wejściowy jest w systemie binarnym.
