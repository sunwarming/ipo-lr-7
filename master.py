# Николай Козик
# Вариант: 4
# Демонстрация пакета collision - Лабораторная работа 10

import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(__file__))

from collision.rect_collision import isCorrectRect, isCollisionRect, intersectionAreaRect, intersectionAreaMultiRect, RectCorrectError

def main():
    print("Лабораторная работа 10: Пакет для работы с прямоугольниками")
    print("=" * 60)
    
    # Демонстрация всех функций
    
    print("\n1. Демонстрация isCorrectRect:")
    rect1 = [(-3.4, 1), (9.2, 10)]
    rect2 = [(-7, 9), (3, 6)]  # Некорректный
    print(f"   isCorrectRect([(-3.4, 1), (9.2, 10)]) = {isCorrectRect(rect1)}")
    print(f"   isCorrectRect([(-7, 9), (3, 6)]) = {isCorrectRect(rect2)}")
    
    print("\n2. Демонстрация isCollisionRect:")
    rect3 = [(-3.4, 1), (9.2, 10)]
    rect4 = [(-7.4, 0), (13.2, 12)]
    rect5 = [(1, 1), (2, 2)]
    rect6 = [(3, 0), (13, 1)]
    try:
        result1 = isCollisionRect(rect3, rect4)
        result2 = isCollisionRect(rect5, rect6)
        print(f"   isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]) = {result1}")
        print(f"   isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]) = {result2}")
    except RectCorrectError as e:
        print(f"   Ошибка: {e}")
    
    print("\n3. Демонстрация intersectionAreaRect:")
    try:
        area1 = intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)])
        area2 = intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)])
        print(f"   intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]) = {area1}")
        print(f"   intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]) = {area2}")
    except (ValueError, RectCorrectError) as e:
        print(f"   Ошибка: {e}")
    
    print("\n4. Демонстрация intersectionAreaMultiRect:")
    rectangles = [
        [(-3, 1), (9, 10)],
        [(-7, 0), (13, 12)], 
        [(0, 0), (5, 5)],
        [(2, 2), (7, 7)]
    ]
    try:
        multi_area = intersectionAreaMultiRect(rectangles)
        print(f"   intersectionAreaMultiRect(4 прямоугольника) = {multi_area}")
    except RectCorrectError as e:
        print(f"   Ошибка: {e}")
    
    print("\n5. Демонстрация обработки ошибок:")
    try:
        isCollisionRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])
    except RectCorrectError as e:
        print(f"   Ошибка RectCorrectError: {e}")
    
    try:
        intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])
    except ValueError as e:
        print(f"   Ошибка ValueError: {e}")
    
    print("\n" + "=" * 60)
    print("Демонстрация завершена!")

if __name__ == "__main__":
    main()