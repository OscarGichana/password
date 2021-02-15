import pyperclip

class User:
    """
    Class that generates new instances of accounts.
    """

    user_list = [] # Empty account list

    def __init__(self,account,first_name,last_name,username,number,email,password):

      # docstring removed for simplicity

        self.account = account
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = number
        self.email = email
        self.password = password



