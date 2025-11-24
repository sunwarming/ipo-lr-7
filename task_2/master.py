# Николай Козик
# Поиск колледжа по названию или краткому названию

import json

print("start code ...")

# Загрузка JSON
try:
    with open("dump.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Файл dump.json не найден.")
    exit()

# Ввод запроса
query = input("Введите название колледжа или его часть: ").strip().lower()

# Поиск
found = False
for item in data:
    if item.get("model") == "data.establishment":
        fields = item.get("fields", {})
        title = fields.get("title", "").lower()
        short_title = fields.get("short_title", "").lower()

        if query in title or query in short_title:
            found = True
            print("\n================== Найдено ==================")
            print(f" Название: {fields.get('title')}")
            print(f" Краткое название: {fields.get('short_title')}")
            print(f" Адрес: {fields.get('adress')}")
            print(f" Телефон: {fields.get('tel')}")
            print(f" Email: {fields.get('email')}")
            print(f" Сайт: {fields.get('wsite')}")
            print(f" Описание: {fields.get('desc')[:300]}...")  # первые 300 символов

if not found:
    print("\n================== не найдено ==================")
    print("Доступные краткие названия:")
    for item in data:
        if item.get("model") == "data.establishment":
            print("-", item.get("fields", {}).get("short_title", "—"))

print("end code ...")
