#code contributed by Akshat-0602
# Program to check if a number is prime or not
from math import sqrt,floor

def prime_check(number):
    if (number == 1):   #if number is equal to 1
        print("1 is neither a prime number nor a composite number.")
    elif (number > 1):  #if number is greater than 1
        for i in range(2, floor(sqrt(number)) + 1):     # 2 is the first prime number
            print(number % i)
            if ((number % i) == 0):           # if the number is divisible by any number other than 1 and itself then it is not a prime number
                print(number, "is not a prime number")      
                print(number, "divided by", i, "=", (number//i))    # print the number of times the number is divisible by the number
                break
        else:   # if the number is not divisible by any number other than 1 and itself
            print(number, "is a prime number.")
    else:       # if the number is less than 1
        print(number, "is not a prime number.")

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    prime_check(num)
