def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
toprint = int(input("Enter number of Fibonacci series terms to be printed: "))
for i in range(0,toprint):
    print(fibonacci(i))