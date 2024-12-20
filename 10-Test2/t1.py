# The playing cards have the following values: Ace (A), 
# King (K), Queen (Q), Jack (J) and 10 (T) 
# have a value of 10 each. 
# The other cards have the value indicated by the card number. 
# Define a function f(player1,player2) that returns true if 
# the first player has cards of the same or higher value, 
# and false otherwise. Example: 

# f ("AJ972","AQT72") -> False 
# f("9532","K8") -> True 

#def f(player1,player2):
   # sum1 = 

def oblicz_wartosc(karty):
    suma = 0
    for karta in karty:
        if karta == 'A' or karta == 'J' or karta == 'K' or karta == 'T' or karta == 'Q':
            suma = suma + 10
        else:
            wartosc = int(karta)
            suma = suma + wartosc
    return suma

def f(player1, player2):
    suma1 = oblicz_wartosc(player1)  # Oblicz wartość kart gracza 1
    suma2 = oblicz_wartosc(player2)  # Oblicz wartość kart gracza 2
    return suma1 >= suma2  # Porównaj wyniki

# Przykłady użycia
print(f("AJ972", "AQT72"))  # False
print(f("9532", "K8"))      # True




