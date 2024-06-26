def get_sum_upto_number_square(last_num):

    total = last_num * (last_num + 1) * (2 * last_num + 1)
    return total // 6


if __name__ == "__main__":

    n = input("Enter a Number to find the sum of squares, upto that number: ")

    try:
        n = int(n)
    except ValueError:
        print("ValueError: Input is not a valid Integer.")
        exit()

    if n > 0:
        result = get_sum_upto_number_square(n)
        print("...")
        print(f"Sum of first {n}^2 natural numbers is {result}.")
    else:
        print("ValueError: Input is a non-positive Integer.")
