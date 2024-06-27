#!/bin/python3


lenght_of_butterfly = int(input("Enter the number of rows and make sure its even "))

n = lenght_of_butterfly//2

print("Generated butterfly pattern is:\n")

for i in range(1,n+1):
    for j in range(1, 2*n+1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print(". ", end="")
    print("")

for i in range(n,0,-1):
    for j in range(2*n,0,-1):
        if j>i and j< 2*n+1-i:
            print("  ", end="")
        else:
            print(". ", end="")
    print("")

