import math

from logic.MainLogic import MainLogic
from models.Employee import Employee

def menu():
        pass

def create():
        # self.header("Create New Contract")

        print(" New Contract: \n\n")
        print(" Personal information\n")

        name = input("\tFull name: ")
        ssn = input("\tEnter ssn: ")
        email = input("\tEnter email: ")
        phone = input("\tEnter mobile phone: ")
        address = input("\tEnter adress: ")
        postal = input("\tEnter postal code: ")
        country_origin = input("\tEnter country of recidence: \n")
        
        print ("Vehicle information\n")
        vehicle_id = input("\tVehicle chosen: ") 
        vehicle_type = input("\tEnter vehicle type")

        print ("\nRental information\n")
        print ('''\33[;34mPlease enter pick-up and drop-off time, use the format dd.mm.yyyy 
        and seperate date and time with a comma\33[;0m
        ''')
        
        date_from = input("\tEnter pick-up date: ")
        date_to = input("\tEnter drop-off date: ")
        # rental_period = start_date + " - " + end_date
        print ("\t\t\33[;36mRental period: \33[;0m", rental_period) 
        contract_made = input ("\tDate of booking: ")
        country = input("\tCountry of rental: ")

        print("\n\n1. Print contract\n2. Modify Contract\n\33[;31mPress q to go back\33[;0m\n")
        action = input("\nChoose an option: ").lower() 

        if action == "1":
                return print_contract()
        if action == "2":
                return modify()
        if action == "q":
                return menu()

def modify():
        pass

def print_contract():
        pass

        
