s = input("Enter a string to be checked from: ")
t = input("Enter string to be checked: ")

if len(s) != len(t):
    print("The string is not valid Anagram")
elif sorted(s, reverse=True) == sorted(t, reverse=True):
    print("The string is valid Anagram")
else:
    print("The string is not valid Anagram")