import math

# Ввод данных
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вычисление среднего арифметического
arithmetic_mean = (num1 + num2) / 2

# Вычисление среднего геометрического
geometric_mean = math.sqrt(num1 * num2)

# Вывод результатов
print(f"Среднее арифметическое: {arithmetic_mean}")
print(f"Среднее геометрическое: {geometric_mean}")
