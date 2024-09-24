from random import choice, randint, shuffle



class PasswordGenerator:
    def __init__(self):
        self.letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def create_password(self):
        password_letters = [choice(self.letter) for _ in range(randint(8, 10))]
        password_symbols = [choice(self.number) for _ in range(randint(2, 4))]
        password_numbers = [choice(self.symbols) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password_join = "".join(password_list)
        return password_join



       
        
        

       

