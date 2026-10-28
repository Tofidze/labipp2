from repository import TransportRepository
from services import TransportService

def main():
    repo = TransportRepository("transport_data.json")
    service = TransportService(repo)

    print("proverka")

    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть весь транспорт")
        print("2. Добавить новый транспорт")
        print("3. Посадить пассажира в транспорт")
        print("0. Выход")
        
        choice = input("Ваш выбор: ")

        if choice == "1":
            vehicles = service.get_all_vehicles()
            if not vehicles:
                print("Автопарк пуст.")
            else:
                print("\n--- Список транспорта ---")
                for v in vehicles:
                    print(f" - {v}")
                    for p in v.passengers:
                        print(f"    * {p}")

        elif choice == "2":
            r_num = input("Введите номер маршрута: ")
            
            try:
                cap = int(input("Введите вместимость (целое число): "))
                
                print("Выберите тип транспорта:")
                print("1 - Автобус")
                print("2 - Трамвай")
                v_type_code = int(input("Ваш выбор (1 или 2): "))
                
                # Передаем данные в слой сервиса
                service.add_vehicle(r_num, cap, v_type_code)
                
            except ValueError:
                print("[Ошибка]: Вместимость и тип транспорта должны быть целыми числами!")

        elif choice == "3":
            r_num = input("Введите номер маршрута транспорта: ")
            p_name = input("Имя пассажира: ")
            t_num = input("Номер билета: ")
            
            service.add_passenger_to_vehicle(r_num, p_name, t_num)

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()