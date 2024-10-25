
decimal_number = 304
binary_string = bin(decimal_number)
print(binary_string)

decimal_number = 304
binary_string = bin(decimal_number)  # Zwraca '0b100110000'
print(binary_string)  # Wynik: 0b100110000

# Bez prefiksu '0b'
binary_string_no_prefix = bin(decimal_number)[2:]
print(binary_string_no_prefix)  # Wynik: 100110000

