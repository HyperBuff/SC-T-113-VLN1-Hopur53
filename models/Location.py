class Location:
    def __init__(self, country, airport, phone, hours, id=None):
        self.country = country
        self.airport = airport
        self.phone = phone
        self.hours = hours
        self.id = id

    def __str__(self):
        return "{}, {}".format(self.country, self.airport)