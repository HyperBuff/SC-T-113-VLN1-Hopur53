
class Customer:
    def __init__(self, name, address, postal, ssn, phone, email, country, id=None) -> None:
        self.name = name
        self.address = address
        self.postal = postal
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.country = country
        self.id = id

    