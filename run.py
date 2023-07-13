# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('travel_planner')

travel = SHEET.worksheet('travel')


def main_menu():
    """
    Display the main menu options
    """
    while True: 
        print("\n==== Travel Planner ====\n")
        print("1. Destination Management")
        print("2. Activity Management")
        print("3. Exit\n")
        print("======================== \n")

        choice = input("Enter your choice: ")
        if choice == '1':
            destination_management() # Add destination management function
        elif choice == '2':
            activity_management() # Add activity management function
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

main_menu()