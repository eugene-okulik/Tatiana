import math

# Ввод данных
cathetus1 = float(input("Введите длину первого катета: "))
cathetus2 = float(input("Введите длину второго катета: "))

# Вычисление гипотенузы
hypotenuse = math.sqrt(cathetus1**2 + cathetus2**2)

# Вычисление площади
area = (cathetus1 * cathetus2) / 2

# Вывод результатов
print(f"Гипотенуза треугольника: {hypotenuse}")
print(f"Площадь треугольника: {area}")
