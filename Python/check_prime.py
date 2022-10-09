#code contributed by manish-9245
# Program to check if a number is prime or not
def prime_check(number):
    if number > 1:
        for i in range(2, number):# 2 is the first prime number
            if (number % i) == 0:# if the number is divisible by any number other than 1 and itself
                print(number, "is not a prime number")# then it is not a prime number
                print(i, "times", number // i, "is", number)# print the number of times the number is divisible by the number
                break
        else:# if the number is not divisible by any number other than 1 and itself
            print(number, "is a prime number")
    else:# if the number is less than 1
        print(number, "is not a prime number")
def main():
    num=int(input("Enter a number: "))
    prime_check(num)
    
if __name__ == '__main__':
    main()