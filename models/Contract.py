

class Contract:
    def __init__(self, customer_id, vehicle_id, employee_id, location_id, date_from, date_to, contract_date, contract_status, pickup_date, dropoff_date, total, paid, id=None) -> None:
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.employee_id = employee_id
        self.location_id = location_id

        self.date_from = date_from
        self.date_to = date_to

        self.contract_date = contract_date
        self.contract_status = contract_status
        self.pickup_date = pickup_date
        self.dropoff_date = dropoff_date
        self.total = total
        self.paid = paid

        self.id = id

    def __str__(self):
        return "Contract for {}".format(self.customer_id)

    def amount_due(self):
        try:
            total = int(self.total)
            paid = int(self.paid)
            return str(total - paid)
        except ValueError:
            return "0"

    #'Edit customer', 'Edit vehicle', 'Edit vehicle status', 'Edit employee id', 'Edit location', 'Edit date from', 'Edit contract status', 'Edit pick up date', 'Edit drop off date'