
class Vehicle:
    def __init__(self, manufacturer, model, vehicle_type_id, status, man_year, color, licence_type, location_id, id = None) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.vehicle_type_id = vehicle_type_id
        self.status = status
        self.man_year = man_year
        self.color = color
        self.licence_type = licence_type
        self.location_id = location_id
        self.id = id


        