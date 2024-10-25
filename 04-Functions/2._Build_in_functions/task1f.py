# integer representing the Unicode code of the € sign
# liczba całkowita reprezentująca kod Unicde znaku €

print(ord('€'))   # Wynik: 65
print(chr(65))    # Wynik: 'A'

# or
symbol = "€"
kod_unicode = ord(symbol)
print(kod_unicode)  # Wynik: 8364

# Odzyskanie symbolu z kodu Unicode
print(chr(8364))  # Wynik: €
