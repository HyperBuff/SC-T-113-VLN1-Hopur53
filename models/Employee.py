
class Employee:
    def __init__(self, role, name, address, postal, ssn, phone, homephone, email, location_id, id = None) -> None:
        self.role = role
        self.name = name
        self.address = address
        self.postal = postal
        self.ssn = ssn
        self.phone = phone
        self.homephone = homephone
        self.email = email
        self.location_id = location_id
        self.id = id

    def __str__(self):
        return self.name