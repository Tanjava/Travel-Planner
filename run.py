# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from art import *

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
    tprint("Travel Planner", font="doom")
    print("Welcome to your personal travel planner!\n")
    while True:

        print("")
         
        print("\n==== Main Travel Menu ====\n")
        print("1. Destination Management")
        print("2. Flight Management")
        print("3. Accommodation Management")
        print("4. Exit\n")
        print("========================== \n")

        choice = input("Enter your choice: \n")
        if choice == '1':
            destination_management()
        elif choice == '2':
            flight_management() 
        elif choice == '3':
            accommodation_management()
        elif choice == '4':
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
        print("1. Add new destination")
        print("2. View destinations")
        print("3. Remove destination")
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

    destination = f"{city}, {country}"
    try: 
        travel.append_row([destination])
        print(f"\nSuccessfully added {destination}!")
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
            print(f"Successfully removed {destination}!")
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
            add_flight_details()
        elif choice == '2':
            view_flight_details()
        elif choice == '3':
            remove_flight_details()
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.")


def add_flight_details():
    """
    Update worksheet, add flight details to specific destination
    """
    print("\n==== Add Flight Details ====\n")
    data = travel.get_all_values()
    try:
        if len(data) <= 1:
            print("\nNo destinations found...\n")
            return

        view_destinations()
        destination_choice = int(input("\nEnter the number of your destination to add your flight details (enter 0 to go back): \n"))

        if destination_choice == 0:
            return

        if destination_choice > 0 and destination_choice <= len(data) - 1:
            destination = data[destination_choice][0]
            airline = input("\nEnter your airline: \n")
            flight_number = input("Enter your flight number: \n")
            departure_date = input("Enter your departure date: \n")
            departure_time = input("Enter your departure time: \n")
            flight_details = f"{airline}, {flight_number}, {departure_date}, {departure_time}"
            travel.update_cell(destination_choice + 1, 2, flight_details)
            print(f"\nSuccessfully added the following flight details for {destination}:\n{flight_details}")
        else:
            print("\nInvalid destination number. Please try again\n")
    except Exception as e:
        print(f"An error occurred while adding your activity: {str(e)}")


def view_flight_details():
    """
    Retrieve and view flight details of specific destination
    """
    print("\n==== View Flight Details ====\n")
    data = travel.get_all_values()
    try:
        if len(data) <= 1:
            print("\nNo destinations found...\n")
            return

        view_destinations()
        destination_choice = int(input("\nEnter the number of your destination to view your flight details (enter 0 to go back): \n"))

        if destination_choice == 0:
            return

        if destination_choice > 0 and destination_choice <= len(data) - 1:
            destination = data[destination_choice][0]
            flight_details = data[destination_choice][1]
            if flight_details:
                airline, flight_number, departure_date, departure_time = flight_details.split(", ")
                print("\n==== View Flight Details ====\n")
                print(f"\u2708  {destination} ")
                print(f"Airline: {airline}")
                print(f"Flight Number: {flight_number}")
                print(f"Departure Date: {departure_date}")
                print(f"Departure Time: {departure_time}")
            else:
                print("\nNo flight details found for this destination.")
        else:
            print("\nInvalid destination number. Please try again")
    except Exception as e:
        print(f"An error occurred while viewing flight details: {str(e)}") 


def remove_flight_details():
    """
    Update worksheet, remove flight details of specific destination
    """
    print("\n==== Remove Flight Details ====\n")
    data = travel.get_all_values()
    try:
        if len(data) <= 1:
            print("\nNo destinations found...\n")
            return

        view_destinations()
        destination_choice = int(input("\nEnter the number of your destination to remove your flight details (enter 0 to go back): \n"))

        if destination_choice == 0:
            return

        if destination_choice > 0 and destination_choice <= len(data) - 1:
            destination = data[destination_choice][0]
            flight_details = data[destination_choice][1]
            if flight_details:
                travel.update_cell(destination_choice +1, 2, "")
                print(f"\nSucessfully removed flight details for {destination}")
            else: 
                print("\nNo flight details found for this destination.")
        else:
            print("\nInvalid destination number. Please try again")
    except Exception as e:
        print(f"An error occurred while viewing flight details: {str(e)}") 


def accommodation_management():
    """
    Display the accommodation management menu options
    """
    while True:
        print("\n==== Accommodation Management ====\n")
        print("1. Add new accommodation details")
        print("2. View accommodation details")
        print("3. Remove accommodation details")
        print("4. Go back to main menu\n")
        print("================================== \n")

        choice = input("Enter your choice: \n")
        if choice == '1':
            add_accommodation_details()
        elif choice == '2':
            view_accommodation_details()
        elif choice == '3':
            remove_accommodation_details()
        elif choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.")


def add_accommodation_details():
    """
    Update worksheet, add accommodation details to specific destination
    """
    print("\n==== Add Flight Details ====\n")
    data = travel.get_all_values()
    try:
        if len(data) <= 1:
            print("\nNo destinations found...\n")
            return

        view_destinations()
        destination_choice = int(input("\nEnter the number of your destination to add your accommodation details (enter 0 to go back): \n"))

        if destination_choice == 0:
            return

        if destination_choice > 0 and destination_choice <= len(data) - 1:
            destination = data[destination_choice][0]
            hotel_name = input("\nEnter your hotel name: \n")
            check_in_date = input("Enter your check-in date: \n")
            check_out_date = input("Enter your check-out date: \n")
            accommodation_details = f"{hotel_name}, {check_in_date}, {check_out_date}"
            travel.update_cell(destination_choice + 1, 3, accommodation_details)
            print(f"\nSuccessfully added the following accommodation details for {destination}:\n{accommodation_details}")
        else:
            print("\nInvalid destination number. Please try again\n")
    except Exception as e:
        print(f"An error occurred while adding your activity: {str(e)}")
    

def view_accommodation_details():
    """
    Retrieve and view accommodation details of specific destination
    """
    print("\n==== View Accommodation Details ====\n")
    data = travel.get_all_values()
    try:
        if len(data) <= 1:
            print("\nNo destinations found...\n")
            return

        view_destinations()
        destination_choice = int(input("\nEnter the number of your destination to view your accommodation details (enter 0 to go back): \n"))

        if destination_choice == 0:
            return

        if destination_choice > 0 and destination_choice <= len(data) - 1:
            destination = data[destination_choice][0]
            accommodation_details = data[destination_choice][2]
            if accommodation_details:
                hotel_name, check_in_date, check_out_date = accommodation_details.split(", ")
                print("\n==== View Accommodation Details ====\n")
                print(f"\u2708  {destination} ")
                print(f"Hotel: {hotel_name}")
                print(f"Check-in Date: {check_in_date}")
                print(f"Check-out Date: {check_out_date}")
            else:
                print("\nNo accommodation details found for this destination.")
        else:
            print("\nInvalid destination number. Please try again")
    except Exception as e:
        print(f"An error occurred while viewing accommodation details: {str(e)}") 

        

main_menu()
