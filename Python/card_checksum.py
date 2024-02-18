# There are a lot of people with credit cards in this world, so card numbers are pretty long.
# Credit card numbers actually have some structure to them. All American Express numbers start with 34 or 37;
# most MasterCard numbers start with 51, 52, 53, 54, or 55 and all Visa numbers start with 4.
# But credit card numbers also have a �checksum� built into them, a mathematical relationship between
# at least one number and others. That checksum enables computers to detect typos (e.g., transpositions),
# if not fraudulent numbers, without having to query a database, which can be slow

# Using Luhn's Algorithm

from sys import exit
from re import match


def main():
    card_number = input("Card Number: ")
    card_numb_len = len(card_number)

    """If input is not digit or not of correct length"""
    if not match(r"^\d{13,16}$", card_number):
        print("INVALID")
        exit(1)

    """If checksum(transposition) fails"""
    if not checksum(card_number, card_numb_len):
        print("INVALID")
        exit(2)

    print(card_brand(card_number, card_numb_len))
    exit(3)


def checksum(card_number, card_numb_len):
    odd_product = 0
    even_add = 0

    """We take every other number starting from second to last, multiply it by 2 and adds them"""
    for odd_num in range(card_numb_len - 2, -1, -2):
        temp = int(card_number[odd_num]) * 2

        """If a product result is greater than 9, i.e. 12, then we want to add 1 and 2 to result, not 12"""
        if temp > 9:
            odd_product += (temp / 10) + (temp % 10)
        else:
            odd_product += temp

    """Now we'll take card numbers that weren't multiplied by 2"""
    for even_num in range(card_numb_len - 1, -1, -2):
        even_add += int(card_number[even_num])

    """If last digit of total result is 0, then checksum passes"""
    if (odd_product + even_add) % 10 == 0:
        return True

    return False


def card_brand(card_number, card_numb_len):
    if card_numb_len == 13 or card_numb_len == 16 and card_number[0] == "4":
        return "VISA"

    elif card_numb_len == 15 and card_number[0:2] == "32" or card_number[0:2] == "37":
        return "AMEX"

    elif (
            card_numb_len == 16
            and 51 <= int(card_number[0:2]) <= 55
    ):
        return "MASTERCARD"

    else:
        return "INVALID"


if __name__ == "__main__":
    main()
