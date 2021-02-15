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


  #find by number
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in account name and returns an account that matches that account name.

        Args:
            account: Username to search for
        Returns :
            Account of person that matches the username.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user



    # user exists?not
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list.
        Args:
            username: account to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                    return True

        return False


        #display all contacts
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list




#copy paste email

  #  @classmethod
    #def copy_password(cls,username):
     #   user_found = User.find_by_username(username)
     #   pyperclip.copy(user_found.password)
     #   User.copy_password()



class Credentials:


     

    credentials_list = []# Empty password list
    def save_credentials(self):
        pass
 
    def __init__(self,password,username):


            self.password = password
            self.username= username
            

            # save_password method saves password objects into password_list
    def save_credentials(self):
        '''
        to save newly created credentials
        '''
        
        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

        

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a credential that matches that password.
        Args:
            password: password to search for
        Returns :
            Credentials of person that matches the password.
        '''

    @classmethod
    def credentials_exist(cls,password):
        '''
        Method that checks if a credentials exists from the contact list.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                    return True

        return False

         
    @classmethod
    def display_all_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list





