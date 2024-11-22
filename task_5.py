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
    else:
        return None 



circle_area = square("circle", 8)
print(f"Площадь круга: {circle_area}")

rectangle_area = square("rectangle", 8, 8)
print(f"Площадь прямоугольника: {rectangle_area}")

triangle_area = square("triangle", 8, 8)
print(f"Площадь треугольника: {triangle_area}")



