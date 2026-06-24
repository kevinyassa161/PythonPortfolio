def division(x, y):
    result = x / y
    return result


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    result = division(num1, num2)
except ValueError:
    print("Введено нечисловое значение!")
except ZeroDivisionError:
    print("В качестве делителя был введён 0!")
else:
    print(f"Результат деления: {result}")
finally:
    print("Работа программы завершена")