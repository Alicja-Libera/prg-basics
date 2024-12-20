def oblicz_wartość(karty):
    suma = 0
    
    for karta in karty:

        if karta in "AKQ":  # "A", "K", and "Q" are worth 15
            suma += 15
        elif karta in "JT":  # "J" is worth 10
            suma += 10
        else:  # For numeric cards
            suma += int(karta)
    
    return suma 

if __name__=="__main__":
    print(oblicz_wartość("AKQ"))  
    print(oblicz_wartość("KQTJ")) 
    print(oblicz_wartość("9532"))
    print(oblicz_wartość("A8Q"))