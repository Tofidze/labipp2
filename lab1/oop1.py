class Passenger:
    def __init__(self, name: str, ticket_number: str):
        self.name = name
        self.ticket_number = ticket_number

    def __str__(self):
        return f"Пассажир: {self.name}, билет: {self.ticket_number}"

class TransportVehicle:
    def __init__(self, route_number: str, capacity: int, vehicle_type: str):
        self.route_number = route_number
        self.capacity = capacity
        self.vehicle_type = vehicle_type
        self.passengers = []

    def add_passenger(self, passenger: Passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Пассажир {passenger.name} сел в транспорт №{self.route_number}")
        else:
            print(f"В транспорте №{self.route_number} нет свободных мест!")

    def __str__(self):
        return f"{self.vehicle_type} №{self.route_number} (Пассажиров: {len(self.passengers)}/{self.capacity})"

class TransportPark:
    def __init__(self, name: str):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle: TransportVehicle):
        self.vehicles.append(vehicle)

    def show_park(self):
        print(f"Автопарк '{self.name}':")
        for v in self.vehicles:
            print(f" - {v}")