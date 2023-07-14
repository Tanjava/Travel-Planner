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

        print("")
         
        print("\n==== Travel Planner ====\n")
        print("1. Destination Management")
        print("2. Flight Management")
        print("3. Exit\n")
        print("======================== \n")

        choice = input("Enter your choice: \n")
        if choice == '1':
            destination_management()
        elif choice == '2':
            flight_management() 
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

        choice = input("Enter your choice: \n")
        if choice == '1':
            add_destination()
        elif choice == '2':
            view_destinations()
        elif choice == '3':
            remove_destination()
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.")

def add_destination():
    """
    Update worksheet, add new row with new destination 
    """
    print("\n==== Add Destination ====\n")
    city = input("Enter the city name: \n")
    country = input("Enter the country name: \n")

    destination = f"{city}, {country}\n"
    try: 
        travel.append_row([destination])
        print(f"\n{destination} added sucessfully!")
    except Exception as e:
        print(f"An error occurred while adding your destination: {str(e)}")


def view_destinations():
    """
    Display destinations with their corresponding index numbers
    """
    print("\n==== Your Destinations ====\n\n")
    data = travel.get_all_values()
    try:
        if len(data) > 1:
            for row in data[1:]:
                index = data.index(row)
                print(f"{index}. {row[0]}\n")
        else:
            print("\nNo destinations found...\n")
    except Exception as e:
        print(f"An error occurred while viewing your destinations: {str(e)}")


def remove_destination():
    """
    Update worksheet, remove the row of a specific destination 
    """
    print("\n==== Remove Destinations ====\n")
    data = travel.get_all_values()
    try:
        if len(data) <= 1:
            print("\nNo destinations found...\n")
            return

        view_destinations()
        del_destination = int(input("Enter the number of the destination you'd like to remove (enter 0 to go back): \n"))

        if del_destination == 0:
            return

        if del_destination > 0 and del_destination <= len(data) - 1:
            destination = data[del_destination][0]
            travel.delete_rows(del_destination + 1)
            print(f"{destination} removed successfully!")
        else:
            print("\nInvalid destination number. Please try again\n")
    except Exception as e:
        print(f"An error occurred while removing the destination: {str(e)}")


def flight_management():
    """
    Display the flight management menu options
    """
    while True:
        print("\n==== Flight Management ====\n")
        print("1. Add new flight details")
        print("2. View flight details")
        print("3. Remove flight details")
        print("4. Go back to main menu\n")
        print("=========================== \n")

        choice = input("Enter your choice: \n")
        if choice == '1':
            add_flight_details() # Add function to add flight details
        elif choice == '2':
            view_flight_details() # Add function to view flight details
        elif choice == '3':
            remove_flight_details() # Add function to remove flight details
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.")



main_menu()