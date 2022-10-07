x = int(input("Enter any number: "))
s = abs(x)
rev_num = 0
while s != 0:
    last_num = s % 10
    rev_num = rev_num * 10 + last_num
    s //= 10
if x == rev_num:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
