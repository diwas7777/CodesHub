# Detects string or binary to convert to vice versa

from sys import exit
from re import sub

# Constants
INPUT_LENGTH = 1000
BINARY_LENGTH = 8


def main():
    # Get user's input, and remove non-alphanumeric characters, to make recognition simple
    user_text = (input("Enter a text or binary value: "))
    if len(user_text) > INPUT_LENGTH:
        print("Length of input too high! Change input size from 'INPUT_LENGTH'!")
        exit(1)
    user_text_only_alpha = sub(r'[^a-zA-Z0-9]', '', user_text)
    user_text_only_binary = user_text.replace(" ", "")

    # Verifying users input if it is binary or string
    converted_result = []
    if check_binary(user_text_only_binary):
        converted_result = binary_to_string(user_text_only_binary)  # Converts binary to ascii to char
    elif user_text_only_alpha.isalnum():
        converted_result = string_to_binary(user_text)  # Coverts char to ascii to binary
    else:
        print("ERROR: Improper input!")
        exit(2)

    # Prints the converted result to user
    print_converted(converted_result)


def check_binary(user_prompt):
    """Checks if given string is binary or not"""
    for char in user_prompt:
        if char not in ('0', '1'):
            return False
    return True


def string_to_binary(input_text):
    """Convert string to ascii then to binary"""
    text_ascii_value = [ord(char) for char in input_text]
    return [format(num, '08b') for num in text_ascii_value]


def binary_to_string(user_text):
    """Converts binary to string"""
    start = 0
    char_list = []
    for i in range(0, len(user_text), 8):  # Loop through binary and covert 8 bits to ascii then to char
        binary = user_text[i: i + BINARY_LENGTH]
        if len(binary) == 8:
            char_list.append(chr(int(binary, 2)))
        else:
            char_list.append(f" 'Failed- [{binary}]'")

    return char_list


def print_converted(converted_result_list):
    """Prints the converted result"""
    print("Output: ")
    for item in converted_result_list:
        print(item, end=" ")  # Remove space from 'end=" "' to print without space


if __name__ == "__main__":
    main()
