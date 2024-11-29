#(p2.py) Define the function f(n1,n2,n3) that returns 
# True if all three numbers n1,n2,n3 are different or False
#otherwise. Sample result:

#f(4,8,5) returns True
#f(2,9,2) returns False


def f(n1, n2, n3):
    return n1 != n2 and n2 != n3 and n1 != n3



def f(n1,n2,n3):
 return n1 != n2 and n2 != n3 and n3 != n1


# Test cases
print(f(4, 8, 5))  # Expected output: True
print(f(2, 9, 2))  # Expected output: False
