import random
import string

class PasswordTools:
    
    def __init__(self) -> None:
        self.my_password = ""
        self.pass_len = len(my_password)

    def __get_upper(self):
        return string.ascii_uppercase[random.randint(0, 25)]

    def __get_lower(self):
        return string.ascii_lowercase[random.randint(0, 25)]

    def __get_number(self):
        avail_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return str(avail_numbers[random.randint(0, len(avail_numbers)-1)])

    def __get_symbol(self):
        avail_symbols = ['!', '(', ')', '?', '[', ']', '_', '`', '~', ';', ':', '@', '#', '$', '%', '^', '&', '*', '+', '=']
        return str(avail_symbols[random.randint(0, len(avail_symbols)-1)])

    def start(self):
        #Ask the user what they would like to do.
        #Currently there is only password generation.
        self.generate_password()
        print(self.get_password())

    def set_options(self):
        # Ask for desired password length
        while(True):
            self.pass_len = input("How long do you want your password? (6-35): ").strip()
            try:
                self.pass_len = int(self.pass_len)
                if(self.pass_len < 6 or self.pass_len > 35):
                    print("Please choose a number between 6-35")
                else:
                    break
            except ValueError:
                print("That is not a number.")

        # Ask for upper and lower case (must choose atleast 1 option)
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

        # Ask for numbers and symbols
        number_bool = input("Do you want numbers? (y/n): ").lower().strip() == 'y'
        symbol_bool = input("Do you want symbols? (y/n): ").lower().strip() == 'y'

        # Create array of chosen options
        pass_options = []
        if(upper_bool):
            pass_options.append(self.__get_upper)
        if(lower_bool):
            pass_options.append(self.__get_lower)
        if(number_bool):
            pass_options.append(self.__get_number)
        if(symbol_bool):
            pass_options.append(self.__get_symbol)

        return pass_options

    # Generate a password with the selected options
    def generate_password(self):
        selected_options = self.set_options()
        # Set first character to a letter
        first_char = []
        if(self.__get_upper in selected_options):
            first_char.append(self.__get_upper)
        if(self.__get_lower in selected_options):
            first_char.append(self.__get_lower)
        self.my_password = first_char[random.randint(0, len(first_char)-1)]()

        # Loop through remaining length
        counter = 1
        while(counter < pass_len):
            self.my_password += selected_options[random.randint(0, len(selected_options)-1)]()
            counter += 1

    def get_password(self):
        return self.my_password

# TODO Calculate password strength
# TODO mutate a password into 1337spk

PasswordTools().start()