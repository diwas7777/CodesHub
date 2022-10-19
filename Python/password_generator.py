import random
import string
# import urllib.request

class PasswordTools:
    
    def __init__(self) -> None:
        self.my_password = ""
        self.pass_len = len(self.my_password)

    def __get_upper(self):
        return random.choice(string.ascii_uppercase)

    def __get_lower(self):
        return random.choice(string.ascii_lowercase)

    def __get_number(self):
        return random.choice(string.digits)

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
                \n\nPlease enter 1, 2, 3, or quit.
                ''')
            if (select_tool == '1'):
                self.generate_password()
                print(self.get_password())
                q = input("Would you like to test this password's strength? (y/n): ").lower().strip() == 'y'
                if(q):
                    print(self.test_strength())
                break
            elif (select_tool == '2'):
                self.leet_mutation()
                print(self.get_password())
                break
            elif (select_tool == '3'):
                print(self.test_strength())
                break
            elif (select_tool == "quit"):
                break
            else:
                print("Please enter 1, 2, 3, or quit.")

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
        if (self.my_password == ""):
            self.my_password = input("Enter the password you wish to mutate:\n")
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

    def test_strength(self):
        if (self.my_password == ""):
            self.my_password = input("Enter the password you wish to test:\n")
        total_points = 7
        score = 0

        # Define all possible characters for passwords using list comprehension.
        # each return true is they are used atleast once in the password.
        upper_case = any([ 1 if character in string.ascii_uppercase else 0 for character in self.my_password ])
        lower_case = any([ 1 if character in string.ascii_lowercase else 0 for character in self.my_password ])
        symbols = any([ 1 if character in string.punctuation else 0 for character in self.my_password ])
        numbers = any([ 1 if character in string.digits else 0 for character in self.my_password ])
        characters = [upper_case, lower_case, symbols, numbers]

        # Check rockyou.txt (common password list used for brute forcing)
        # # Also forcing lowercase as attackers can easily find small variations from words in this list.
        # rockyou_url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
        # rockyou_file = urllib.request.urlopen(rockyou_url)
        # if self.my_password.lower() in rockyou_file:
        #     return (f"Password found in common list, 0/{str(total_points)}")

        # Give points based on length of password.
        length = len(self.my_password)
        if length >= 26:
            score += 4
        elif length >= 18:
            score += 3
        elif length >= 12:
            score += 2
        elif length >= 8:
            score +=1
        print(f"Password length is {str(length)}, adding {str(score)} points.")

        # Give points based on variation used.
        # No points if less than 2 variants are used.
        if sum(characters) > 3:
            score += 3
        elif sum(characters) > 2:
            score += 2
        elif sum(characters) > 1:
            score += 1
        print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points.")

        # Calculate strength based on points earned.
        if score < 4:
            return(f"The password is very weak. Score: {str(score)} / {str(total_points)}")
        elif score == 4:
            return(f"The password is ok. Score: {str(score)} / {str(total_points)}")
        elif score > 4 and score < 6:
            return(f"The password is good! Score: {str(score)} / {str(total_points)}")
        else:
            return(f"The password is strong! Score: {str(score)} / {str(total_points)}")        

PasswordTools().start()