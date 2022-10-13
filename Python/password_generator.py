import random
import string

class PasswordTools:
    
    def __init__(self) -> None:
        self.my_password = ""
        self.pass_len = len(self.my_password)

    def __get_upper(self):
        return random.choice(string.ascii_uppercase)

    def __get_lower(self):
        return random.choice(string.ascii_lowercase)

    def __get_number(self):
        avail_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return str(random.choice(avail_numbers))

    def __get_symbol(self):
        avail_symbols = ['!', '(', ')', '?', '[', ']', '_', '`', '~', ';', ':', '@', '#', '$', '%', '^', '&', '*', '+', '=']
        return str(random.choice(avail_symbols))

    def start(self):
        #Ask the user what they would like to do.
        while(True):
            select_tool = input('''Welcome to PasswordTools\nWhat would you like to do?
                \n 1) Generate a new password.
                \n 2) Change a password to l33tspeak.
                \n 3) Check the strength of your password.
                \n\nPlease enter 1, 2, or 3.
                ''')
            if (select_tool == '1'):
                self.generate_password()
                print(self.get_password())
                break
            elif (select_tool == '2'):
                self.leet_mutation()
                print(self.get_password())
                break
            elif (select_tool == '3'):
                #self.check_strenght()
                #break
                print("Sorry, this tool hasn't been implemented yet.")
            else:
                print("Please enter 1, 2, or 3")

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
        self.my_password = random.choice(first_char)()
        # self.my_password = first_char[random.randint(0, len(first_char)-1)]()

        # Loop through remaining length
        counter = 1
        while(counter < self.pass_len):
            self.my_password += random.choice(selected_options)()
            # self.my_password += selected_options[random.randint(0, len(selected_options)-1)]()
            counter += 1

    def get_password(self):
        return self.my_password

    # Ask for a password and mutate it into l33tspeak
    def leet_mutation(self):
        self.my_password = input("Enter the password you wish to mutate")
        leet_map = {
            'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
            'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
            'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
            'v': ['\\/']
            }
        leet_pass = ""
        for char in self.my_password:
            if (char.lower() in leet_map):
                leet_pass += random.choice(leet_map[char.lower()])
            else:
                leet_pass += char.lower()
        self.my_password = leet_pass
        
# TODO Calculate password strength        

PasswordTools().start()