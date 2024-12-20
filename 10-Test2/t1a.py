# Write a program that takes a single string of 
# playing cards (like "AJ972") and calculates the t
# otal value of the cards. The values are as follows:


# A, K, Q, J, and T each have a value of 10.
# The other cards have a value equal to their number
#  (2 to 9).
# For example:

# If the input is "AJ972", the total value should be 38.
# If the input is "K8", the total value should be 18.

def oblicz_wartość(karty):
 
    suma=0 
    
    for karta in karty:
        if karta == "J" or karta == "A" or karta == "K":
            suma = suma + 10 
        else:
            suma += int(karta)
    return suma

if __name__ == "__main__":
    print(oblicz_wartość("AJ972"))  # Example 1: Should print 38
    print(oblicz_wartość("K8"))     # Example 2: Should print 18
