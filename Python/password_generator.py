import random
import string

avail_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
avail_symbols = ['!', '(', ')', '?', '[', ']', '_', '`', '~', ';', ':', '@', '#', '$', '%', '^', '&', '*', '+', '=']

# Take user input for type of password
def set_options():
    global pass_len
    global upper_bool
    global lower_bool
    global number_bool
    global symbol_bool
    while(True):
        pass_len = input("How long do you want your password? (6-35): ").strip()
        try:
            pass_len = int(pass_len)
            if(pass_len < 6 or pass_len > 35):
                print("Please choose a number between 6-35")
            else:
                break
        except ValueError:
            print("That is not a number.")
            

    upper_bool = input("Do you want uppercase letters? (y/n): ").lower().strip() == 'y'
    lower_bool = input("Do you want lowercase letters? (y/n): ").lower().strip() == 'y'
    while (not upper_bool and not lower_bool):
        print ("You must select atleast upper or lower case")
        ans = (input("(upper, lower, both): ").lower().strip())
        if(ans == 'upper'):
            upper_bool = True
        elif(ans == 'lower'):
            lower_bool = True
        elif(ans == 'both'):
            upper_bool = True
            lower_bool = True
        else:
            print ("I don't understand.")
    number_bool = input("Do you want numbers? (y/n): ").lower().strip() == 'y'
    symbol_bool = input("Do you want symbols? (y/n): ").lower().strip() == 'y'

def chosen_options():
    set_options()
    print("Password will be " + str(pass_len) + " characters long, and contain:")
    print("\tUppercase Letters: " + str(upper_bool))
    print("\tLowercase Letters: " + str(lower_bool))
    print("\tNumbers: " + str(number_bool))
    print("\tSymbols: " + str(symbol_bool))

# Generate password of just letters
def generate_simple_password():
    global my_password
    my_password = ""
    counter = 0
    while(counter < pass_len):
        if(upper_bool and lower_bool):
            flip = randint(0, 1)
            if(flip):
                my_password += string.ascii_uppercase[random.randint(0, 25)]
            else:
                my_password += string.ascii_lowercase[random.randint(0, 25)]
        elif(upper_bool):
            my_password += string.ascii_uppercase[random.randint(0, 25)]
        else:
            my_password += string.ascii_lowercase[random.randint(0, 25)]
        counter += 1

# TODO generate password based on all inputs
# TODO Calculate password strength
# TODO mutate a password into 1337spk

set_options()
generate_simple_password()
print(my_password)