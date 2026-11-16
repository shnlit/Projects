import math

def calculate_distance(x1, y1, x2, y2):
    '''Рассчитывает расстояние между двумя точками'''
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance

def calculate_triangle_area(a, b, c):
    '''Вычисляет площадь треугольника по формуле Герона'''
    p = (a + b + c) / 2
    triangle_area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return triangle_area

x1, y1 = map(float, input("Введите координаты точки A (x y): ").split())
x2, y2 = map(float, input("Введите координаты точки B (x y): ").split())
x3, y3 = map(float, input("Введите координаты точки C (x y): ").split())

ab = calculate_distance(x1, y1, x2, y2)
bc = calculate_distance(x2, y2, x3, y3)
ac = calculate_distance(x1, y1, x3, y3)

area = calculate_triangle_area(ab, bc, ac)

print(f"Площадь треугольника: {area:.2f}")