# Python Program to print Fibonacci Sequence upto n terms

n = int(input("Please enter the number of terms : "))

# Base Condition(First 2 terms)
n1, n2 = 0, 1
cnt = 0

# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif n == 1:
   print("Fibonacci Sequence upto ",n," :")
   print(n1)
# Generate Fibonacci Sequence
else:
   print("Fibonacci Sequence : ")
   while cnt < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       cnt += 1

# So Fibonacci Sequence is what we know a sequence where every term 
# is the sum of preceding two terms (Except first two terms : 0 and 1)
# So here we implement this program by using 3 simple conditions : 
# 1. If the input terms is less or than equal 0, we output this as wrong input
# 2. If the input is 1 , we output the the first term i.e. n1
# 3. Other wise, 
#              we use n1 and n2 repeatedly until cnt < n 
#              print n1 which is the next term in the sequence
#              store n1 + n2 in nth
#              and update the n1 and n2 as the last two terms accordingly i.e. with n2 and nth
#              update cnt by adding 1. 