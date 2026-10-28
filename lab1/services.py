from models import TransportVehicle, Passenger
from repository import TransportRepository

class TransportService:
    def __init__(self, repository: TransportRepository):
        self.repository = repository
        self.vehicles = self.repository.load_data()

    def add_vehicle(self, route_number: str, capacity: int, vehicle_type: str) -> bool:
        
    def add_vehicle(self, route_number: str, capacity: int, vehicle_type_code: int) -> bool:
        
        allowed_types = {
            1: "Автобус",
            2: "Трамвай"
        }

        if vehicle_type_code not in allowed_types:
            print(f"Неверный тип транспорта! Введите 1 (Автобус) или 2 (Трамвай).")
            return False

        vehicle_type = allowed_types[vehicle_type_code]

        for v in self.vehicles:
            if v.route_number == route_number:
                print(f"Транспорт с маршрутом №{route_number} уже существует в автопарке!")
                return False

        new_vehicle = TransportVehicle(route_number, capacity, vehicle_type)
        self.vehicles.append(new_vehicle)
        self.repository.save_data(self.vehicles)
        print(f"{vehicle_type} №{route_number} успешно добавлен в автопарк.")
        return True


    def add_passenger_to_vehicle(self, route_number: str, name: str, ticket_number: str) -> bool:
        target_vehicle = None
        for v in self.vehicles:
            if v.route_number == route_number:
                target_vehicle = v
                break

        if not target_vehicle:
            print(f"Транспорт с маршрутом №{route_number} не найден.")
            return False

        if len(target_vehicle.passengers) >= target_vehicle.capacity:
            print(f"В транспорте №{route_number} нет свободных мест!")
            return False

        passenger = Passenger(name, ticket_number)
        target_vehicle.passengers.append(passenger)
        self.repository.save_data(self.vehicles)
        print(f"Пассажир {name} сел в транспорт №{route_number}.")
        return True

    def get_all_vehicles(self) -> list:
        return self.vehicles