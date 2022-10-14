import random
import secrets
import string


def generate_password(length=None):
    all_characters = list(
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    # to set password length, if not given.
    if not length:
        length = random.randint(12, 25)

    # we shuffle the 'all_characters' list few times.
    for i in range(length // 3):
        random.shuffle(all_characters)

    # add random characters one by one in 'password' and return it.
    password = ""
    for i in range(length):
        password += secrets.choice(all_characters)

    return password


if __name__ == "__main__":
    new_pass = generate_password()
    print("Generated a Random Password:")
    print(new_pass)
