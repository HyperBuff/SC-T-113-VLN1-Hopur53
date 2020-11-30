
class Contract:
    def __init__(self, name, phone, email, address, date_from, date_to, vehicle_id, location, vehicle_status, employee_id, loan_date, return_date, total, loan_status) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

        self.vehicle_id = vehicle_id
        self.vehicle_status = vehicle_status

        self.employee_id = employee_id
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.loan_date = loan_date
        self.loan_status = loan_status
        self.return_date = return_date

        self.total = total



