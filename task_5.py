import numpy as np

def square(shape, *args):
    
    if shape == "circle":
        radius = args[0]
        return np.pi * radius**2
    elif shape == "rectangle":
        width, height = args
        return width * height
    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height



shape = input("Выберите фигуру (circle, rectangle, triangle): ").lower()

if shape == "circle":
    radius = float(input("Введите радиус: "))
    area = square("circle", radius)
    print(f"Площадь круга: {area}")
elif shape == "rectangle":
    width = float(input("Введите ширину: "))
    height = float(input("Введите высоту: "))
    area = square("rectangle", width, height)
    print(f"Площадь прямоугольника: {area}")
elif shape == "triangle":
    base = float(input("Введите основание: "))
    height = float(input("Введите высоту: "))
    area = square("triangle", base, height)
    print(f"Площадь треугольника: {area}")










