lst = []
i = 0
m = int(input("Enter number of elements to add in list: "))
while i<m:
    n = int(input("Enter a number: "))
    lst.append(n)
    i = i+1
print(lst)
print(list(reversed(lst)))
x = int(input("Enter number to find: "))
if x in lst:
    print(f"Number {x} is in the list at position {lst.index(x)}")
else:
    print(f"Number {x} is not in the list")