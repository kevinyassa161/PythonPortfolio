def pluse(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


try:
    print("Сложение")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except ValueError:
    print("Введено нечисловое значение!")
else:
    print(f"Результат сложения: {pluse(num1, num2)}")

try:
    print("\nВычитание")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except ValueError:
    print("Введено нечисловое значение!")
else:
    print(f"Результат вычитания: {minus(num1, num2)}")

try:
    print("\nУмножение")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
except ValueError:
    print("Введено нечисловое значение!")
else:
    print(f"Результат умножения: {multiple(num1, num2)}")

try:
    print("\nДеление")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result_div = division(num1, num2)
except ValueError:
    print("Введено нечисловое значение!")
except ZeroDivisionError:
    print("Деление на 0 запрещено!")
else:
    print(f"Результат деления: {result_div}")
