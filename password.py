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


#saving accounts
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)


  #delete
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)


