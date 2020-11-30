

def get_input():
    user_input = input("Choose Option: ")

def display_main_menu():

    MENU = ('''----------- Admin Menu ------------ 

1. Employee Management 
2. Vehicle Management
3. Contract Management
4. Location Management
5. Financial Management
9. Back to Main Menu 
''')

    print (MENU)    

def main_menu_options():
    
    if user_input == 1 :
        return display_employee_menu()
    if user_input == 2 : 
        return display_vehicle_management()
    if user_input == 3 : 
        return display_contract_management()
    if user_input == 4 :
        return display_location_management()
    if user_input == 5 :
        return display_financial_management()
    if user_input == 9 : 
        return display_main_menu()
    else : 
        print ("Wrong Entry")

def display_employee_menu():
    EMPLOYEE = ('''----------- Employees -------------
    1. Booking Employees
    2. Delivery Employees
    9. Back to Main Menu
    ''')

    print (EMPLOYEE)

def employee_options():
    if user_input == 1 :
        return display_booking_employee_menu()
    if user_input == 2 : 
        return display_delivery_employee_menu()
    if user_input == 9 :
        display_main_menu
    else :
        print ("Wrong Entry")

def display_booking_employee_menu():
    BOOKING_EMPLOYEE = ('''-------- Booking Employee ---------
1. Contract management
2. Rental rates management
9. Back to Main Menu
''')

    print (BOOKING_EMPLOYEE)
    
def booking_employee_options():
    
    if user_input == 1 :
        return display_contract_management
    if user_input == 2 :
        return rental_rates_management
    if user_input == 9 :
        return display_main_menu
    else :
        print ("Wrong Entry")

def display_delivery_employee_menu():
    DELIVERY_EMPLOYEE = ('''-------- Delivery Employee --------
1. Contracts
2. Vehicles
3. Locations
9. Back to Main Menu
''')

    print (DELIVERY_EMPLOYEE)

def delivery_employee_options():
    if user_input == 1 :
        return contracts
    if user_input == 2 :
        return vehicles 
    if user_input == 3 :
        return locations
    if user_input == 9 : 
        return display_main_menu
    else : 
        print ("Wrong Entry")

def display_vehicle_management():
    pass

def display_contract_management():
    pass

def display_location_management():
    pass

def display_financial_management():
    pass
    
    

#main
#ser_input = get_input()
display_main_menu()
main_menu_options()
