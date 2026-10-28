import json
import os
from models import Route, Ticket, Bus, Plane, Train

class TransportRepository:
    def __init__(self, filename: str = "transport_system.json"):
        self.filename = filename

    def load_data(self) -> list:
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                vehicles = []
                for item in data:
                    r_data = item["route"]
                    route = Route(r_data["route_id"], r_data["departure"], r_data["arrival"])
                    
                    v_type = item["vehicle_type"]
                    v_num = item["vehicle_number"]
                    cap = item["capacity"]

                    if v_type == "Автобус":
                        vehicle = Bus(v_num, cap, route)
                    elif v_type == "Самолёт":
                        vehicle = Plane(v_num, cap, route, airline="Госавиа")
                    elif v_type == "Поезд":
                        vehicle = Train(v_num, cap, route, carriages_count=10)
                    else:
                        continue

                    for t_data in item.get("tickets", []):
                        ticket = Ticket(
                            t_data["ticket_id"],
                            t_data["passenger_name"],
                            t_data["passenger_id"],
                            t_data["seat_number"]
                        )
                        vehicle.tickets.append(ticket)

                    vehicles.append(vehicle)
                return vehicles
        except Exception as e:
            print(f"[Ошибка чтения файла]: {e}")
            return []

    def save_data(self, vehicles: list):
        try:
            data = [v.to_dict() for v in vehicles]
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"[Ошибка записи файла]: {e}")