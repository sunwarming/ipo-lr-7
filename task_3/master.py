# Николай Козик
# Вариант: 4
# Программа для управления записями о машинах (улучшенная версия с валидацией)

import json
import os

FILE_NAME = "cars.json"
operations_count = 0

def initialize_data():
    """Инициализация начальных данных"""
    global operations_count
    try:
        if not os.path.exists(FILE_NAME):
            initial_data = [
                {"id": 1, "name": "Model S", "manufacturer": "Tesla", "is_petrol": False, "tank_volume": 0},
                {"id": 2, "name": "Camry", "manufacturer": "Toyota", "is_petrol": True, "tank_volume": 60},
                {"id": 3, "name": "A4", "manufacturer": "Audi", "is_petrol": True, "tank_volume": 55},
                {"id": 4, "name": "Leaf", "manufacturer": "Nissan", "is_petrol": False, "tank_volume": 0},
                {"id": 5, "name": "X5", "manufacturer": "BMW", "is_petrol": True, "tank_volume": 85}
            ]
            save_cars_data(initial_data)
            operations_count += 1
            print("✓ Создан файл с 5 начальными записями")
    except Exception as e:
        print(f"❌ Ошибка инициализации: {e}")

def load_cars_data():
    """Загрузка данных из JSON файла"""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"❌ Ошибка загрузки данных: {e}")
        return []

def save_cars_data(cars):
    """Сохранение данных в JSON файл"""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(cars, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Ошибка сохранения: {e}")
        return False

def get_valid_string(prompt, min_length=1):
    """Получение корректной строки от пользователя"""
    while True:
        try:
            value = input(prompt).strip()
            if len(value) >= min_length:
                return value
            print(f"❌ Поле должно содержать не менее {min_length} символа")
        except Exception as e:
            print(f"❌ Ошибка ввода: {e}")

def get_valid_int(prompt, min_val=None, max_val=None):
    """Получение корректного целого числа"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"❌ Значение должно быть не меньше {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Значение должно быть не больше {max_val}")
                continue
            return value
        except ValueError:
            print("❌ Пожалуйста, введите целое число")
        except Exception as e:
            print(f"❌ Ошибка ввода: {e}")

def get_valid_bool(prompt):
    """Получение корректного булевого значения"""
    while True:
        try:
            value = input(prompt).strip().lower()
            if value in ['да', 'yes', 'true', '1', 'д', 'y']:
                return True
            elif value in ['нет', 'no', 'false', '0', 'н', 'n']:
                return False
            else:
                print("❌ Пожалуйста, введите 'да' или 'нет'")
        except Exception as e:
            print(f"❌ Ошибка ввода: {e}")

def generate_new_id(cars):
    """Генерация нового ID для записи"""
    if not cars:
        return 1
    return max(car["id"] for car in cars) + 1

def display_car_info(car, position=None):
    """Отображение информации о машине"""
    fuel_type = "Бензин" if car["is_petrol"] else "Электричество"
    if position:
        print(f"\n{position}. ID: {car['id']}")
    else:
        print(f"\nID: {car['id']}")
    print(f"   Модель: {car['name']}")
    print(f"   Производитель: {car['manufacturer']}")
    print(f"   Тип топлива: {fuel_type}")
    print(f"   Объем бака: {car['tank_volume']} л")
    print("-" * 40)

def show_all_cars():
    """Вывод всех записей"""
    global operations_count
    cars = load_cars_data()
    
    if not cars:
        print("❌ Нет записей о машинах")
        return
    
    print("\n" + "="*50)
    print("ВСЕ ЗАПИСИ О МАШИНАХ:")
    print("="*50)
    
    for i, car in enumerate(cars, 1):
        display_car_info(car, i)
    
    operations_count += 1
    print(f"Всего записей: {len(cars)}")

def find_car_by_id():
    """Поиск машины по ID"""
    global operations_count
    cars = load_cars_data()
    
    if not cars:
        print("❌ Нет записей о машинах")
        return
    
    car_id = get_valid_int("Введите ID машины для поиска: ", 1)
    
    found = False
    for position, car in enumerate(cars, 1):
        if car["id"] == car_id:
            print(f"\nНАЙДЕНА ЗАПИСЬ (позиция в списке: {position}):")
            print("="*50)
            display_car_info(car)
            found = True
            operations_count += 1
            break
    
    if not found:
        print("❌ Запись с таким ID не найдена!")

def add_new_car():
    """Добавление новой машины"""
    global operations_count
    cars = load_cars_data()
    
    print("\nДОБАВЛЕНИЕ НОВОЙ МАШИНЫ:")
    print("-" * 30)
    
    new_id = generate_new_id(cars)
    name = get_valid_string("Введите название модели: ", 2)
    manufacturer = get_valid_string("Введите производителя: ", 2)
    is_petrol = get_valid_bool("Машина бензиновая? (да/нет): ")
    
    if is_petrol:
        tank_volume = get_valid_int("Введите объем бака (л): ", 1, 200)
    else:
        tank_volume = 0
    
    new_car = {
        "id": new_id,
        "name": name,
        "manufacturer": manufacturer,
        "is_petrol": is_petrol,
        "tank_volume": tank_volume
    }
    
    cars.append(new_car)
    
    if save_cars_data(cars):
        print("✓ Машина успешно добавлена!")
        operations_count += 1
    else:
        print("❌ Ошибка при сохранении данных")

def delete_car_by_id():
    """Удаление машины по ID"""
    global operations_count
    cars = load_cars_data()
    
    if not cars:
        print("❌ Нет записей о машинах")
        return
    
    car_id = get_valid_int("Введите ID машины для удаления: ", 1)
    
    initial_count = len(cars)
    cars = [car for car in cars if car["id"] != car_id]
    
    if len(cars) < initial_count:
        if save_cars_data(cars):
            print("✓ Машина успешно удалена!")
            operations_count += 1
        else:
            print("❌ Ошибка при сохранении данных")
    else:
        print("❌ Машина с таким ID не найдена!")

def show_menu():
    """Отображение главного меню"""
    print("\n" + "="*40)
    print("УПРАВЛЕНИЕ ЗАПИСЯМИ О МАШИНАХ")
    print("="*40)
    print("1. Вывести все записи")
    print("2. Вывести запись по ID")
    print("3. Добавить запись")
    print("4. Удалить запись по ID")
    print("5. Выйти из программы")
    print("="*40)

def main_menu():
    """Главная функция меню"""
    global operations_count
    
    initialize_data()
    
    while True:
        show_menu()
        choice = get_valid_string("Выберите пункт меню (1-5): ", 1)
        
        if choice == "1":
            show_all_cars()
        elif choice == "2":
            find_car_by_id()
        elif choice == "3":
            add_new_car()
        elif choice == "4":
            delete_car_by_id()
        elif choice == "5":
            print(f"\nПрограмма завершена.")
            print(f"Всего выполнено операций: {operations_count}")
            break
        else:
            print("❌ Неверный выбор. Пожалуйста, выберите от 1 до 5.")

# Запуск программы
if __name__ == "__main__":
    print("Программа управления записями о машинах")
    print("Все вводимые данные проверяются на корректность")
    main_menu()