import json
import os
from models import TransportVehicle, Passenger

class TransportRepository:
    def __init__(self, filename: str = "transport_data.json"):
        self.filename = filename

    def load_data(self) -> list:
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                vehicles = []
                for item in data:
                    vehicle = TransportVehicle(
                        route_number=item["route_number"],
                        capacity=item["capacity"],
                        vehicle_type=item["vehicle_type"]
                    )
                    for p_data in item.get("passengers", []):
                        vehicle.passengers.append(Passenger(p_data["name"], p_data["ticket_number"]))
                    vehicles.append(vehicle)
                return vehicles
        except Exception as e:
            print(f"Ошибка чтения файла: {e}")
            return []

    def save_data(self, vehicles: list):
        try:
            data = [v.to_dict() for v in vehicles]
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка записи файла: {e}")