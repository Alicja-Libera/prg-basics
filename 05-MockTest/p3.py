#(p3.py) A text contains any number of words. Define a function f(name) 
# that returns the acronym (first letters of all words). Sample result:

#f("Internet of Things") returns "loT"
#f("For Your Information") returns "FYI" f("Python") returns "p"

def f(name):
    words = name.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

print(f("Internet of Things") )


def f(name):
 words=name.split()
 acronym=''.join(word[0].upper() for word in words)
 return acronym 

    
    
