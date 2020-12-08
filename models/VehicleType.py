
class VehicleType:
    def __init__(self, name: str, location_id: str, rate: str, id = None) -> None:
        self.name = name
        self.location_id = location_id
        self.rate = rate
        self.id = id

    def __str__(self):
        return self.name

    