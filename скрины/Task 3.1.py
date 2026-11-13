import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return distance

def dots_input():
    x, y = map(float, input("Введите координаты точки (x y): ").split())
    return x, y

x1, y1 = dots_input()
x2, y2 = dots_input()
distance = calculate_distance(x1, y1, x2, y2)
print(f"Расстояние от первой точки до второй, отрезок 1 - {distance:.2f}м.")

x1, y1 = dots_input()
x2, y2 = dots_input()
distance = calculate_distance(x1, y1, x2, y2)
print(f"Расстояние от первой точки до второй, отрезок 2 - {distance:.2f}м.")

x1, y1 = dots_input()
x2, y2 = dots_input()
distance = calculate_distance(x1, y1, x2, y2)
print(f"Расстояние от первой точки до второй, отрезок 3 - {distance:.2f}м.")
