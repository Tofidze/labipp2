import json

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


if __name__ == "__main__":

    park = TransportPark("Городской Транспорт")

    bus = TransportVehicle(route_number="101", capacity=2, vehicle_type="Автобус")
    tram = TransportVehicle(route_number="5", capacity=20, vehicle_type="Трамвай")

    park.add_vehicle(bus)
    park.add_vehicle(tram)

    p1 = Passenger("Иван", "T-01")
    p2 = Passenger("Анна", "T-02")
    p3 = Passenger("Петр", "T-03")

    bus.add_passenger(p1)
    bus.add_passenger(p2)
    bus.add_passenger(p3)

    print()
    park.show_park()


data = {
    "route": bus.route_number,
    "capacity": bus.capacity,
    "passengers": [{"name": p.name, "ticket": p.ticket_number} for p in bus.passengers]
}
with open("transport.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open("transport.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("Загружено из JSON:", loaded_data)