#!/usr/bin/env python3.8

from password import User
import pyperclip


def create_user(account,fname,lname,uname,phone,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(account,fname,lname,uname,phone,email,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def check_existing_users(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def copy_password():
    '''
    Function that copies details to clipboard
    '''
    return User.copy_password()

def main():
  '''
  Main function
  '''
  print("Hello Welcome to your PASSWORD LOCKER. What is your name?")
  user_name = input()

  print(f"Hello {user_name}. what would you like to do?")
  print('\n')

  while True:
          print("Use these short codes : cu - create a new user, du - display user, fu -find a user, del -delete a user, ex -exit the password locker ")

          short_code = input().lower()

          if short_code == 'cu':
                  print("New User")
                  print("-"*10)

                  print ("Which account would you like to create?")
                  account = input()

                  print ("First name ....")
                  f_name = input()

                  print("Last name ...")
                  l_name = input()

                  print("Username ...")
                  u_name = input()


                  print("Phone number ...")
                  p_number = input()

                  print("Email address ...")
                  e_address = input()

                  print("Password ...")
                  p_word = input()



                  save_users(create_user(account,f_name,l_name,u_name,p_number,e_address,p_word)) # create and save new user.
                  print ('\n')
                  print(f"New User {u_name} {f_name} created")
                  print ('\n')

          elif short_code == 'du':

                  if display_users():
                          print("Here is a list of all your users")
                          print('\n')

                          for user in display_users():
                                  print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                          print('\n')
                  else:
                          print('\n')
                          print("You dont seem to have any user saved yet")
                          print('\n')

          elif short_code == 'fu':

                  print("Enter the username you want to search for")

                  search_account = input()
                  if check_existing_users(search_account):
                          search_user = find_user(search_account)
                          print(f"{search_user.first_name} {search_user.last_name}")
                          print('-' * 20)

                          print(f"Phone number.......{search_user.phone_number}")
                          print(f"Email address.......{search_user.email}")
                  else:
                          print("That contact does not exist")





if __name__ == '__main__':

    main()
