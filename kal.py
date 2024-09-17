def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Целая часть от деления")
        print("6. Остаток от деления")
        print("7. Возведение в степень")
        print("0. Выход")

        try:
            choice = int(input("Введите номер операции: "))
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        if choice == 0:
            print("Выход из программы.")
            break

        if choice not in range(1, 8):
            print("Неверный выбор. Попробуйте снова.")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Пожалуйста, введите корректные числа.")
            continue

        if choice == 1:
            result = num1 + num2
            print(f"Результат сложения: {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"Результат вычитания: {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"Результат умножения: {result}")
        elif choice == 4:
            if num2 == 0:
                print("Ошибка: Деление на ноль.")
            else:
                result = num1 / num2
                print(f"Результат деления: {result}")
        elif choice == 5:
            if num2 == 0:
                print("Ошибка: Деление на ноль.")
            else:
                result = num1 // num2
                print(f"Целая часть от деления: {result}")
        elif choice == 6:
            if num2 == 0:
                print("Ошибка: Деление на ноль.")
            else:
                result = num1 % num2
                print(f"Остаток от деления: {result}")
        elif choice == 7:
            result = num1 ** num2
            print(f"Результат возведения в степень: {result}")

if __name__ == "__main__":
    calculator()