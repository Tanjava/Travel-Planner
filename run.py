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
data = travel.get_all_values()


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
            destination_management()
        elif choice == '2':
            activity_management() # Add activity management function
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

def destination_management():
    """
    Display the destination management menu options
    """
    while True:
        print("\n==== Destination Management ====\n")
        print("1. Add a new destination")
        print("2. View destinations")
        print("3. Remove a destination")
        print("4. Go back to main menu\n")
        print("================================ \n")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_destination()
        elif choice == '2':
            view_destinations()
        elif choice == '3':
            remove_destination() # Add the remove destination function
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.")

def add_destination():
    """
    Update worksheet, add new row with new destination 
    """
    print("\n==== Add Destination ====\n")
    city = input("Enter the city name: ")
    country = input("Enter the country name: ")

    destination = f"\n{city}, {country}"
    try: 
        travel.append_row([destination])
        print(f"{destination} added sucessfully!")
    except Exception as e:
        print(f"An error occurred while adding your destination: {str(e)}")


def view_destinations():
    """
    View the user's destinations
    """
    print("\n==== Your Destinations ====")
    try:
        if len(data) > 1:
            for row in data[1:]:
                print(row[0])
        else:
            print("\nNo destinations found...")
    except Exception as e:
        print(f"An error occurred while viewing your destinations: {str(e)}")


main_menu()