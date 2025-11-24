# Николай Козик
# Вариант: 4
# Программа для управления записями о машинах

import json

FILE = "cars.json"

def load_data():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def show_all(data):
    print("\n Все записи:")
    for car in data:
        print(f"ID: {car['id']}, Модель: {car['name']}, Производитель: {car['manufacturer']}, "
              f"Бензин: {'Да' if car['is_petrol'] else 'Нет'}, Объём бака: {car['tank_volume']} л")

def show_by_field(data):
    field = input("Введите имя поля (name, manufacturer, is_petrol, tank_volume): ")
    value = input("Введите значение для поиска: ")
    print("\n Найденные записи:")
    for car in data:
        if str(car.get(field)).lower() == value.lower():
            print(car)

def add_record(data):
    try:
        new_id = max(car["id"] for car in data) + 1 if data else 1
        name = input("Название модели: ")
        manufacturer = input("Производитель: ")
        is_petrol = input("Бензиновая? (да/нет): ").strip().lower() == "да"
        tank_volume = int(input("Объём бака (л): "))
        new_car = {
            "id": new_id,
            "name": name,
            "manufacturer": manufacturer,
            "is_petrol": is_petrol,
            "tank_volume": tank_volume
        }
        data.append(new_car)
        save_data(data)
        print(" Запись добавлена.")
    except Exception as e:
        print("Ошибка при добавлении:", e)

def delete_by_field(data):
    field = input("Введите имя поля для удаления: ")
    value = input("Введите значение: ")
    new_data = [car for car in data if str(car.get(field)).lower() != value.lower()]
    if len(new_data) < len(data):
        save_data(new_data)
        print(" Записи удалены.")
    else:
        print(" Ничего не найдено для удаления.")

def menu():
    data = load_data()
    while True:
        print("\n Меню:")
        print("1. Показать все записи")
        print("2. Показать записи по полю")
        print("3. Добавить запись")
        print("4. Удалить запись по полю")
        print("5. Выход")
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            show_all(data)
        elif choice == "2":
            show_by_field(data)
        elif choice == "3":
            add_record(data)
            data = load_data()
        elif choice == "4":
            delete_by_field(data)
            data = load_data()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print(" Неверный ввод. Попробуйте снова.")

print("start code ...")
menu()
print("end code ...")
