
class Contract:
<<<<<<< HEAD
    def __init__(self, name, ssn, phone, email, address, vehicle_id, vehicle_status, employee_id, location, date_from, date_to, loan_date, loan_status, return_date, total, id=None) -> None:
=======
    def __init__(self, name, phone, email, address, vehicle_id, vehicle_status, employee_id, location_id, date_from, date_to, loan_date, loan_status, return_date, total, id = None):
>>>>>>> 124bc1435e4e9031a2f343517a40286dedd15f3a
        self.name = name
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.address = address

        self.vehicle_id = vehicle_id
        self.vehicle_status = vehicle_status

        self.employee_id = employee_id
        self.location_id = location_id
        self.date_from = date_from
        self.date_to = date_to
        self.loan_date = loan_date
        self.loan_status = loan_status
        self.return_date = return_date

        self.total = total
        self.id = id