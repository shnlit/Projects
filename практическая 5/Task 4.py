Pi = 3.14159

def calculate_rectangle_area(width, height):
    '''Рассчитывает площадь прямоугольника'''
    return width * height

def calculate_circle_area(radius):
    '''Рассчитывает площадь круга'''
    return Pi * radius ** 2

width, height = map(float, input("Введите стороны прямоугольника: ").split())
square_area = calculate_rectangle_area(width, height)
print(f'Площадь прямоугольника - {square_area:.1f}')

radius = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(radius)
print(f'Площадь круга - {circle_area:.1f}')