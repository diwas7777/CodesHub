def get_sum_upto_number(last_num):
    # we will update this variable in each iteration, with the total sum.
    total = 0

    # iterating from 'last_num' to '0' using while loop.
    # we add each number in 'total' and deduct 1 from 'last_num'
    while True:
        if last_num == 0:
            break
        total += last_num
        last_num -= 1

    return total


if __name__ == "__main__":
    # asks for an Input from User, raises an error if input is not a Valid Number.
    n = input("Enter a Number to find the sum, upto that number: ")

    try:
        n = int(n)
    except ValueError:
        print("ValueError: Input is not a valid Integer.")
        exit()

    # run, if input is a positive integer.
    if n > 0:
        # calling the function above, with users's input as argument.
        result = get_sum_upto_number(n)
        print("...")
        print(f"Sum of first {n} natural numbers is {result}.")
    else:
        print("ValueError: Input is a non-positive Integer.")
