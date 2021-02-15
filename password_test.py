import unittest # Importing the unittest module
from password import User # Importing the user class
from password import Credentials  #importing the credentials class
import sys, pyperclip

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Twitter","James","Muriuki","OG","0712345678","james@ms.com","123") # create object object



#init test
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.username,"OG")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.assertEqual(self.new_user.password,"123")


#saving contact
    def test_save_user(self):
        '''
        test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


#adding 1 contact
    def tearDown(self):
            '''
            method that does clean up after each test case has run.
            '''
            User.user_list = [] #creating empty list

#adding multiple contacts
    def test_save_multiple_user(self):
            '''
            to check if we can save multiple user objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = User("account","Test","user","username","0712345678","test@user.com","password") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

# delete
    def test_delete_user(self):
            '''
            to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("account","Test","user","username","0712345678","test@user.com","password")
            test_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_list),1)

#find by username
    def test_find_user_by_username(self):
            '''
            test to check if we can find a user by their username and display information
            '''

            self.new_user.save_user()
            test_user = User("account","Test","user","username","0711223344","test@user.com","password") # new contact
            test_user.save_user()

            found_user = User.find_by_username("username")

            self.assertEqual(found_user.password,test_user.password)

#check if contact exists
    def test_user_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the user.
            '''

            self.new_user.save_user()
            test_user = User("account","Test","user","username","0711223344","test@user.com","password")
            test_user.save_user()

            user_exists = User.user_exist("username")

            self.assertTrue(user_exists)


#display all contacts
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentiasls class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        self.new_credentials =Credentials ("123","username")

    def test_init(self):
        self.assertEqual(self.new_credentials.password,"123")
        self.assertEqual(self.new_credentials.username,"username")




if __name__ == '__main__':
    unittest.main()