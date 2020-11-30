
class Employee:
    def __init__(self, name, address, postal, ssn, phone, homephone, email, id = None) -> None:
        self.name = name
        self.address = address
        self.postal = postal
        self.ssn = ssn
        self.phone = phone
        self.homephone = homephone
        self.email = email
        self.id = id
    
    def set_id(self, id):
        self.id = id
