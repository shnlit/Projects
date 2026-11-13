import math

x1, y1 = map(float, input("Введите координаты первой точки (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты второй точки (x2 y2): ").split())

distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
print(f"Расстояние от первой точки до второй - {distance:.2f}")
