def calculate_step(name, operation_type, num1, num2):
    if operation_type == "+":
        print(f"Результат сложения: {num1 + num2}\n")
    if operation_type == "-":
        print(f"Результат вычитания: {num1 - num2}\n")
    if operation_type == "*":
        print(f"Результат умножения: {num1 * num2}\n")
    if operation_type == "/":
        print(f"Результат деления: {num1 / num2}\n")


def run_calculate(name, operation_type):
    print(f"Операция: {name}")
    try:
        num1 = float(input("Введите первое число "))
        num2 = float(input("Введите второе число "))

        result = calculate_step(name, operation_type, num1, num2)
    except ValueError:
        print("Введено нечисловое значение!")
    except ZeroDivisionError:
        print("Деление на 0 запрещено!")


run_calculate("Сложение", "+")
run_calculate("Вычитание", "-")
run_calculate("Умножение", "*")
run_calculate("Деление", "/")
