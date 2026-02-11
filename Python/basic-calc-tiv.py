# LANGUAGE: Python 
# ENV: Python 3.12
# AUTHOR: Tivisha Sinha
# GITHUB: https://github.com/ti-v/hacktoberfest

# Adds four procedures for adding, subtracting, dividing, and multiplying
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

# Prompts the user to type in a number 1-4 in order to select the operation they wish the two numbers to be multiplied by
print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

# Sets variable "sel" to whichever number the user choice earlier. "sel" implies the user's "selection."
sel = int(input("Select operation (1-4): "))

# Prompts the user to type in the numbers they wish to have added, multiplied, divided, or subtracted. Each number will be stored as a variable. 
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# This is where it all comes together! Adds, multiples, subtracts, or divides the two numbers based on the user's selection earlier. The equation will be printed out.
if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", div(n1, n2))

# This is an error message that is shown if the user typed in something that was not a number 1-4 and therefore cannot be stored as "sel"
else:
    print("Invalid input. Please type in a number 1-4.")
    
