import queue
# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put(2)    
cards.put(3)  
cards.put(7)     
cards.put(4)    
cards.put(1)  
cards.put(9)  
cards.put(8)  


## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# Pobranie ostatnich dwóch elementów i obliczenie ich sumy
last1 = cards.get()
last2 = cards.get()

the_last_2 = last1 + last2

print(f'The sum of last two is : {the_last_2}')
# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)