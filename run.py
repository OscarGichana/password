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


if __name__ == '__main__':

    main()
