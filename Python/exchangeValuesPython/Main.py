#Declaring variables
a = 1
b = 3

#Printing the assigned values
print(f"The old value of a is {a}")
print(f"The old value of b is {b}\n")

#To shift the values, we need another variable i.e c

c = b #First, we will put the value of b in c
b = a #Second, we will put the value of a in b (b is empty due to 'First')
a = c #Now we will put value of c in a

#Lets print new values
print(f"The new value of a is {a}")
print(f"The new value of b is {b}")