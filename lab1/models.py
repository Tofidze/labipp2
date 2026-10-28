class Route:
    def __init__(self, route_id: str, departure: str, arrival: str):
        self.route_id = route_id
        self.departure = departure
        self.arrival = arrival

    def to_dict(self) -> dict:
        return {"route_id": self.route_id, "departure": self.departure, "arrival": self.arrival}

    def __str__(self):
        return f"Маршрут {self.route_id}: {self.departure} -> {self.arrival}"


class Ticket:
    def __init__(self, ticket_id: str, passenger_name: str, passenger_id: str, seat_number: int):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.passenger_id = passenger_id
        self.seat_number = seat_number

    def to_dict(self) -> dict:
        return {
            "ticket_id": self.ticket_id,
            "passenger_name": self.passenger_name,
            "passenger_id": self.passenger_id,
            "seat_number": self.seat_number
        }

    def __str__(self):
        return f"Билет №{self.ticket_id} | Место: {self.seat_number} | Пассажир: {self.passenger_name}"


class TransportVehicle:
    def __init__(self, vehicle_number: str, capacity: int, route: Route, vehicle_type: str):
        self.vehicle_number = vehicle_number
        self.capacity = capacity
        self.route = route
        self.vehicle_type = vehicle_type
        self.tickets = []

    def to_dict(self) -> dict:
        return {
            "vehicle_type": self.vehicle_type,
            "vehicle_number": self.vehicle_number,
            "capacity": self.capacity,
            "route": self.route.to_dict(),
            "tickets": [t.to_dict() for t in self.tickets]
        }

    def __str__(self):
        return f"{self.vehicle_type} №{self.vehicle_number} [{self.route}] (Мест: {len(self.tickets)}/{self.capacity})"


class Bus(TransportVehicle):
    def __init__(self, vehicle_number: str, capacity: int, route: Route, is_intercity: bool = True):
        super().__init__(vehicle_number, capacity, route, vehicle_type="Автобус")
        self.is_intercity = is_intercity


class Plane(TransportVehicle):
    def __init__(self, vehicle_number: str, capacity: int, route: Route, airline: str):
        super().__init__(vehicle_number, capacity, route, vehicle_type="Самолёт")
        self.airline = airline


class Train(TransportVehicle):
    def __init__(self, vehicle_number: str, capacity: int, route: Route, carriages_count: int):
        super().__init__(vehicle_number, capacity, route, vehicle_type="Поезд")
        self.carriages_count = carriages_count