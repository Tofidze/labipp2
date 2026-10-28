from repository import TransportRepository
from services import TransportService

def main():
    repo = TransportRepository("transport_system.json")
    service = TransportService(repo)

    print("check")

    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть весь транспорт и проданные билеты")
        print("2. Зарегистрировать новый транспорт (Автобус / Самолёт / Поезд)")
        print("3. Забронировать/купить билет на рейс")
        print("0. Выход")
        
        choice = input("Ваш выбор: ")

        if choice == "1":
            vehicles = service.get_all_vehicles()
            if not vehicles:
                print("В компании пока нет транспорта.")
            else:
                print("\n--- Реестр транспорта и рейсов ---")
                for v in vehicles:
                    print(f" * {v}")
                    for t in v.tickets:
                        print(f"      - {t}")

        elif choice == "2":
            v_num = input("Введите номер транспорта")
            
            try:
                cap = int(input("Введите общую вместимость мест: "))
                
                print("\nВыберите тип транспорта:")
                print("1 - Автобус")
                print("2 - Самолёт")
                print("3 - Поезд")
                v_type_code = int(input("Ваш выбор: "))

                print("\nДоступные маршруты:")
                for code, route in service.get_routes().items():
                    print(f"{code} - {route}")
                route_code = int(input("Выберите код маршрута: "))

                service.add_vehicle(v_num, cap, v_type_code, route_code)

            except ValueError:
                print("Вместимость и коды должны быть целыми числами")

        elif choice == "3":
            v_num = input("Введите номер транспорта, на который берется билет ")
            t_id = input("Уникальный номер билета ")
            name = input("ФИО пассажира: ")
            p_id = input("Номер паспорта / ID пассажира: ")
            
            try:
                seat = int(input("Номер желаемого места: "))
                service.book_ticket(v_num, t_id, name, p_id, seat)
            except ValueError:
                print("Номер места должен быть числом")

        elif choice == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()