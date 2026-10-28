class Passenger:
    def __init__(self, name: str, ticket_number: str):
        self.name = name
        self.ticket_number = ticket_number

    def to_dict(self) -> dict:
        return {"name": self.name, "ticket_number": self.ticket_number}

    def __str__(self):
        return f"Пассажир: {self.name}, билет: {self.ticket_number}"


class TransportVehicle:
    def __init__(self, route_number: str, capacity: int, vehicle_type: str):
        self.route_number = route_number
        self.capacity = capacity
        self.vehicle_type = vehicle_type
        self.passengers = []

    def to_dict(self) -> dict:
        return {
            "route_number": self.route_number,
            "capacity": self.capacity,
            "vehicle_type": self.vehicle_type,
            "passengers": [p.to_dict() for p in self.passengers]
        }

    def __str__(self):
        return f"{self.vehicle_type} №{self.route_number} (Пассажиров: {len(self.passengers)}/{self.capacity})"