import numpy as np

def squar(shape):
    
    if shape == 'circle':
        radius = input("Радиус круга: ")
        squar = np.pi * radius**2
        print(squar)
    elif shape == 'rectangle':
        length = input("Длина прямоугольника: ")
        width = input("Ширина прямоугольника: ")
        squar = width * length
        print(squar)
    elif shape == 'triangle':
        height = input("Высота треугольника: ")
        footing = input("Основание треугольника: ")
        squar = (height * footing) * 0,5
        print(squar)
    return squar

print(squar)


    