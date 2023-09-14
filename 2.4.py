try:
    dividend = float(input("Введите делимое: "))
    divisor = float(input("Введите делитель: "))
    result = dividend / divisor
    print(f"Результат деления: {result}")
except ValueError:
    print("Ошибка ввода данных. Пожалуйста, введите числа.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")
finally:
    print("Завершение работы программы.")
