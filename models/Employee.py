
class Employee:
    def __init__(self, role, name, address, postal, ssn, phone, homephone, email, id, location = None) -> None:
        self.role = role
        self.name = name
        self.address = address
        self.postal = postal
        self.ssn = ssn
        self.phone = phone
        self.homephone = homephone
        self.email = email
        self.id = id
        self.location = location