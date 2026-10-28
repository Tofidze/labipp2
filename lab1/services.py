from models import Route, Ticket, Bus, Plane, Train
from repository import TransportRepository

class TransportService:
    def __init__(self, repository: TransportRepository):
        self.repository = repository
        self.vehicles = self.repository.load_data()
        
        self.available_routes = {
            1: Route("A-B", "Москва", "Санкт-Петербург"),
            2: Route("A-C", "Москва", "Казань"),
            3: Route("A-D", "Москва", "Сочи"),
            4: Route("B-D", "Санкт-Петербург", "Сочи")
        }

    def add_vehicle(self, vehicle_number: str, capacity: int, type_code: int, route_code: int) -> bool:

        if route_code not in self.available_routes:
            print("Неверный код маршрута")
            return False
        route = self.available_routes[route_code]

        for v in self.vehicles:
            if v.vehicle_number == vehicle_number:
                print(f"Транспорт с номером {vehicle_number} уже зарегистрирован")
                return False

        if type_code == 1:
            vehicle = Bus(vehicle_number, capacity, route)
        elif type_code == 2:
            vehicle = Plane(vehicle_number, capacity, route, airline="SkyLines")
        elif type_code == 3:
            vehicle = Train(vehicle_number, capacity, route, carriages_count=8)
        else:
            print("Неверный тип транспорта (введите 1, 2 или 3).")
            return False

        self.vehicles.append(vehicle)
        self.repository.save_data(self.vehicles)
        print(f"{vehicle.vehicle_type} №{vehicle_number} добавлен на маршрут {route.route_id}.")
        return True

    def book_ticket(self, vehicle_number: str, ticket_id: str, name: str, passenger_id: str, seat: int) -> bool:
        target_vehicle = None
        for v in self.vehicles:
            if v.vehicle_number == vehicle_number:
                target_vehicle = v
                break

        if not target_vehicle:
            print(f"Транспорт с номером {vehicle_number} не найден")
            return False

        if len(target_vehicle.tickets) >= target_vehicle.capacity:
            print(f"На этот рейс нет свободных мест (полная вместимость)")
            return False


        for t in target_vehicle.tickets:
            if t.seat_number == seat:
                print(f"Место №{seat} уже занято!")
                return False
            if t.ticket_id == ticket_id:
                print(f"Билет с номером {ticket_id} уже существует!")
                return False

        new_ticket = Ticket(ticket_id, name, passenger_id, seat)
        target_vehicle.tickets.append(new_ticket)
        self.repository.save_data(self.vehicles)
        print(f"Билет №{ticket_id} успешно оформлен для {name} на место №{seat}.")
        return True

    def get_all_vehicles(self) -> list:
        return self.vehicles

    def get_routes(self) -> dict:
        return self.available_routes