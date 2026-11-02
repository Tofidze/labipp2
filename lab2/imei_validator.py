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

def process_user_input():
    user_input = input("Введите IMEI")
    if luhn_check(user_input):
        print(f"'{user_input}' является правильным")
    else:
        print(f"'{user_input}' неправльный (неверный формат или не прошел проверку луны")

if __name__ == "__main__":
    while True:
        print("\n=== Меню проверки IMEI ===")
        print("1. Проверить IMEI с клавиатуры")
        print("2. Выход")
        
        choice = input("Выберите действие")        
        if choice == '1':
            process_user_input()
        elif choice == '2':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")