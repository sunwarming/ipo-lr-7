"""
Модуль для работы с пересечениями прямоугольников
Лабораторная работа 10
"""

class RectCorrectError(ValueError):
    """Ошибка некорректного прямоугольника"""
    pass

def isCorrectRect(rect):
    """
    Проверяет корректность прямоугольника.
    
    Args:
        rect: список из двух кортежей [(x1,y1), (x2,y2)]
        
    Returns:
        bool: True если прямоугольник корректен, иначе False
    """
    if not isinstance(rect, list) or len(rect) != 2:
        return False
        
    try:
        (x1, y1), (x2, y2) = rect
        if x1 >= x2 or y1 >= y2:
            return False
        return True
    except (TypeError, ValueError):
        return False

def isCollisionRect(rect1, rect2):
    """
    Проверяет пересекаются ли два прямоугольника.
    
    Args:
        rect1: первый прямоугольник
        rect2: второй прямоугольник
        
    Returns:
        bool: True если пересекаются, иначе False
        
    Raises:
        RectCorrectError: если прямоугольник некорректен
    """
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некорректный")
    
    (x11, y11), (x12, y12) = rect1
    (x21, y21), (x22, y22) = rect2
    
    # Проверяем пересечение по осям
    x_collision = x12 >= x21 and x22 >= x11
    y_collision = y12 >= y21 and y22 >= y11
    
    return x_collision and y_collision

def intersectionAreaRect(rect1, rect2):
    """
    Вычисляет площадь пересечения двух прямоугольников.
    
    Args:
        rect1: первый прямоугольник
        rect2: второй прямоугольник
        
    Returns:
        float: площадь пересечения, 0 если не пересекаются
        
    Raises:
        ValueError: если прямоугольник некорректен
    """
    if not isCorrectRect(rect1) or not isCorrectRect(rect2):
        raise ValueError("Некорректный прямоугольник")
    
    if not isCollisionRect(rect1, rect2):
        return 0.0
    
    (x11, y11), (x12, y12) = rect1
    (x21, y21), (x22, y22) = rect2
    
    # Вычисляем пересечение по осям
    x_left = max(x11, x21)
    x_right = min(x12, x22)
    y_bottom = max(y11, y21)
    y_top = min(y12, y22)
    
    width = x_right - x_left
    height = y_top - y_bottom
    
    return width * height

def intersectionAreaMultiRect(rectangles):
    """
    Вычисляет общую площадь пересечения множества прямоугольников.
    
    Args:
        rectangles: список прямоугольников
        
    Returns:
        float: общая площадь пересечения
        
    Raises:
        RectCorrectError: если любой прямоугольник некорректен
    """
    if not rectangles:
        return 0.0
    
    # Проверяем все прямоугольники на корректность
    for i, rect in enumerate(rectangles):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Прямоугольник {i+1} некорректен")
    
    if len(rectangles) == 1:
        # Для одного прямоугольника - его площадь
        (x1, y1), (x2, y2) = rectangles[0]
        return (x2 - x1) * (y2 - y1)
    
    # Находим общее пересечение всех прямоугольников
    x_left = max(rect[0][0] for rect in rectangles)
    x_right = min(rect[1][0] for rect in rectangles)
    y_bottom = max(rect[0][1] for rect in rectangles) 
    y_top = min(rect[1][1] for rect in rectangles)
    
    # Если нет общего пересечения
    if x_left >= x_right or y_bottom >= y_top:
        return 0.0
    
    width = x_right - x_left
    height = y_top - y_bottom
    
    return width * height