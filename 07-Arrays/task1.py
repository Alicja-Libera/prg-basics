arr = [2, 3, 7, 5, 4]

Number_of_elements = len(arr) 
print('Number of elements', Number_of_elements)

First_value= arr[0]
print('First value:', First_value)

nd_value= arr[1]
print('Second value:', nd_value)

last_value= arr[-1]
print('Last value:', last_value)

last_value_nd = arr[4]
print("Last value but not negative:", last_value_nd)

sum= arr[0]+arr[-4]
print('Sum of the first and last value:', sum )

middle= arr[(len(arr)-1)//2]
print('The middle value is:' , middle)

for value in arr:
    print(value, end=" ") 

#the array - done!
#number of elements - done!
#first value - done!
#second value - done!
#last value -done!
#last but one value (do not use negative index values) - done! 
#sum of the first and last value - done!
#middle value - done!
#all array values separated by a single space (use a loop statement)

#Tip: to read the last value of an array use array[len(array)-1] or array[-1]