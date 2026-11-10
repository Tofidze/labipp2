import re

def luhn_check(imei: str) -> bool:
    if not isinstance(imei, str) or not re.fullmatch(r'\d{15}', imei):
        return False
    
    digits = [int(c) for c in imei]
    s = 0
    is_second = False
    
    for i in range(len(digits) - 1, -1, -1):
        d = digits[i]
        if is_second:
            d *= 2
            if d > 9:
                d -= 9
        s += d
        is_second = not is_second
        
    return s % 10 == 0

def find_imeis_in_text(text: str) -> list:
    pattern = r'\b\d{15}\b'
    potential_imeis = re.findall(pattern, text)
    
    valid_imeis = [imei for imei in potential_imeis if luhn_check(imei)]
    return valid_imeis

def process_user_input():
    user_input = input("Введите IMEI")
    if luhn_check(user_input):
        print(f"'{user_input}' правильный")
    else:
        print(f"'{user_input}' неправльный")

def process_file(filepath: str):
    print(f"\n Поиск IMEI в файле {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        valid_imeis = find_imeis_in_text(content)
        
        if valid_imeis:
            print(f"Найдено корректных IMEI: {len(valid_imeis)}")
            for imei in valid_imeis:
                print(f"  • {imei}")
        else:
            print("Корректных IMEI в файле нет")
            
    except FileNotFoundError:
        print(f"файл '{filepath}' не найден.")
    except Exception as e:
        print(f"ошибка при чтении файла: {e}")

if __name__ == "__main__":
    while True:
        print("\n=== Меню проверки IMEI ===")
        print("1. Проверить IMEI с клавиатуры")
        print("2. Найти IMEI в файле")
        print("3. Выход")
        
        choice = input("Выберите действие")        
        if choice == '1':
            process_user_input()
        elif choice == '2':
            path = input("Введите путь к текстовому файлу").strip()
            process_file(path)
        elif choice == '3':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")