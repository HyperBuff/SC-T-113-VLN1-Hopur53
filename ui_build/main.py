

def get_input():
    user_input = int(input("Choose Option: "))
    return user_input

def display_main_menu():
    MAIN_MENU = (''' 
------------ Main Menu ------------

        1. Booking Employee
        2. Delivery Employee
        3. Mechanic Employee
        4. Financial Employee
        5. Admin
        9. Quit
''')
    print (MAIN_MENU)

def main_menu_options():
    user_input = get_input()

    if user_input == 1 :
        return display_booking_employee_menu(), booking_employee_options()
    if user_input == 2 : 
        return display_delivery_employee_menu(), delivery_employee_options()
    if user_input == 3 :
        return mechanic_employee_menu(), mechanic_employee_options()
    if user_input == 4 :
        return display_financial_management(), financial_management_options()
    if user_input == 5 : 
        return display_admin_menu(), admin_menu_options()
    if user_input == 9 :
        return quit 

def mechanic_employee_menu():
    return display_vehicle_management

def mechanic_employee_options():
    return vehicle_management_options

def display_financial_employee_menu():
    return display_financial_management()

def financial_employee_options():
    return financial_employee_options()

def display_admin_menu():

    ADMIN_MENU = ('''
----------- Admin Menu ------------ 

1. Employee Management 
2. Vehicle Management
3. Contract Management
4. Location Management
5. Financial Management
9. Back to Main Menu 
''')

    print (ADMIN_MENU)    

def admin_menu_options():
    user_input = get_input()

    if user_input == 1 :
        return display_employee_menu(), employee_options()
    if user_input == 2 : 
        return display_vehicle_management(), vehicle_management_options()
    if user_input == 3 : 
        return display_contract_management(), contract_management_options()
    if user_input == 4 :
        return display_location_management(), location_management_options()
    if user_input == 5 :
        return display_financial_management(), financial_management_options()
    if user_input == 9 : 
        return display_admin_menu(), admin_menu_options()
    else : 
        print ("Wrong Entry")


def display_employee_menu():
    EMPLOYEE = ('''
----------- Employees -------------

1. Booking Employees
2. Delivery Employees
9. Back to Main Menu
''')

    print (EMPLOYEE)

def employee_options():
    user_input = get_input()

    if user_input == 1 :
        return display_booking_employee_menu(), booking_employee_options()
    if user_input == 2 : 
        return display_delivery_employee_menu(), delivery_employee_options()
    if user_input == 9 :
        display_admin_menu(), admin_menu_options()
    else :
        print ("Wrong Entry")

def display_booking_employee_menu():
    BOOKING_EMPLOYEE = ('''
-------- Booking Employee ---------

1. Contract management
2. Rental rates management
9. Back to Main Menu
''')

    print (BOOKING_EMPLOYEE)
    
def booking_employee_options():
    user_input = get_input()

    if user_input == 1 :
        return display_contract_management(), contract_options()
    if user_input == 2 :
        return rental_rates_management(), rental_rate_option()
    if user_input == 9 :
        return display_main_menu(), main_menu_options()
    else :
        print ("Wrong Entry")

def rental_rates_management():
    RENTAL_RATES = ('''
----- Rental Rate Management ------

1. Register rental rate
2. Modify rental rate
3. View rental rate
9. Back to Contract Management
''')

    print (RENTAL_RATES)

def rental_rate_option():
    user_input = get_input()
    if user_input == 1 :
        return register_rental_rate()
    if user_input == 2 :
        return modify_rental_rate()
    if user_input == 3 :
        return display_rental_rate()
    if user_input == 9 :
        return display_admin_menu(), admin_menu_options()

def register_rental_rate():
    REGISTERED_RENTAL_RATE = ('''1. Vehicle type
2. Rate per day
9. Back to Rental Rate Management
''')
#Vantar Save dæmið
    print (REGISTERED_RENTAL_RATE)

def registered_rental_rate():
    user_input = get_input()
    if user_input == 1 :
       # return input_vehicle_type()
    if user_input == 2 :
        #return input_rental_rate() 
    if user_input == 9 :
        #return rental_rate_options()
    else :
        print ("Wrong Entry")

def vehicle_rate_info_dict():
    typ = input("Please input a type: ") 
    rate = input("Plesse input a rate: ") 
    class_list = {typ : rate}

    return class_list

def vehicle_rate_info_dict_save():
    '''Setja vehicle_rate_dict inn í txt file'''
    pass

def modify_rental_rate():
    pass

def display_rental_rate():
    pass

def display_delivery_employee_menu():
    DELIVERY_EMPLOYEE = ('''
-------- Delivery Employee --------

1. Contracts
2. Vehicles
3. Locations
9. Back to Main Menu
''')

    print (DELIVERY_EMPLOYEE)

def delivery_employee_options():
    user_input = get_input()

    if user_input == 1 :
        return contracts
    if user_input == 2 :
        return vehicles 
    if user_input == 3 :
        return locations
    if user_input == 9 : 
        return display_admin_menu
    else : 
        print ("Wrong Entry")

def contracts():
    pass

def contract_options():
    pass 

def vehicles():
    pass

def locations():
    pass

def display_vehicle_management():
    VEHICLE = (''' 
------- Vehicle Management --------

1. Register New Vehicle
2. Modify Vehicle Information
3. View Vehicle Information
4. View Vehicle Status
9. Back to Admin Menu
''')

    print (VEHICLE)

def vehicle_management_options():
    user_input = get_input()

    if user_input == 1 :
        return register_new_vehicle()
    if user_input == 2 :
        return modify_vehicle_info()
    if user_input == 3 : 
        return display_vehicle_info()
    if user_input == 4 :
        return display_vehicle_status()
    if user_input == 9 :
        return display_admin_menu(), admin_menu_options()
    else :
        print ("Wrong entry")

def register_new_vehicle():
    pass

def modify_vehicle_info():
    pass

def display_vehicle_info():
    pass

def display_vehicle_status():
    pass

def display_contract_management():
    CONTRACT_MENU = ('''
------------ Contracts ------------

1. Create new contract
2. Modify contract
3. View contract
''')

    print (CONTRACT_MENU)

def contract_management_options():
    user_input = get_input()

    if user_input == 1 :
        return create_new_contract()
    if user_input == 2 :
        return modify_contract()
    if user_input == 3 : 
        return display_contract()
    if user_input == 9 :
        return display_admin_menu(), admin_menu_options()
    else :
        print ("Wrong Entry")

def create_new_contract():
    pass

def modify_contract():
    pass

def display_contract():
    pass

def display_location_management():
    LOCATION = (''' 
------- Location Management -------

1. Modify Location information
2. Create new location
3. View Location information
4. View opening hour overview
9. Back to Admin Menu 
''')

    print (LOCATION)

def location_management_options():
    user_input = get_input()

    if user_input == 1 : 
        return modify_location_info()
    if user_input == 2 :
        return create_new_location()
    if user_input == 3 :
        return display_location_info()
    if user_input == 4 : 
        return view_opening_hour_overview()
    if user_input == 9 : 
        return display_admin_menu(), admin_menu_options()

def modify_location_info():
    pass

def create_new_location():
    pass

def display_location_info():
    pass

def view_opening_hour_overview():
    pass

def display_financial_management():
    FINANCIAL = ('''
------ Financial Management -------

1. Unpaid contracts
2. Closed contracts
3. Financial reports
9. Back to Financial Employee
''')

    print (FINANCIAL)

def financial_management_options():
    user_input = get_input()

    if user_input == 1 :
        return unpaid_contracts()
    if user_input == 2 :
        return closed_contracts()
    if user_input == 3 :
        return financial_reports()
    if user_input == 9 :
        return display_admin_menu(), admin_menu_options()

def unpaid_contracts():
    total_amount = int(input("Please enter the total amount"))
    amount_paid = int(input("Please input amount paid"))
    amount_due = total_amount-amount_paid
    
    UNPAID = ('''
---------- Unpaid Contract ----------

Total amount : {}
Amount paid  : {}     

Amount due   : {}''').format(total_amount, amount_paid, amount_due)    

    OPTIONS = ('''
1. Print Invoice
2. Settle Invoice
9. Back to Financial Management
''')

    print (UNPAID,OPTIONS)
    user_input = get_input()

    if user_input == 1 :
        return display_invoice
    if user_input == 2 : 
        return modify_invoice
    if user_input == 9 :
        return display_financial_management, financial_management_options
 
def display_invoice():
    pass

def modify_invoice():
    pass 

def closed_contracts():
    pass

def financial_reports():
    REPORTS = ('''
-------- Financial Report ---------

1. Branches Report
2. Utilization Report
3. Invoice Overview 

9. Back to Financial Management
''')

    print (REPORTS)

def financial_report_options():
    user_input = get_input()

    if user_input == 1 :
        return branches_report()
    if user_input == 2 :
        return utilization_report()
    if user_input == 3 :
        return invoice_overview()
    if user_input == 9 :
        return display_financial_management(),financial_management_options()

def branches_report():
    pass

def utilization_report():
    pass

def invoice_overview():
    pass



#main
#ser_input = get_input()
display_admin_menu()
admin_menu_options()
employee_options()
display_booking_employee_menu()
booking_employee_options()
