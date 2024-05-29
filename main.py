def add(x, y):
    """
       Adds two numbers and returns the result.

       @param x: First number
       @param y: Second number
       @return: Sum of x and y
       """
    return x + y

def subtract(x, y):
    """
       Subtracts the second number from the first and returns the result.

       @param x: First number
       @param y: Second number
       @return: Difference of x and y
       """
    return x - y

def multiply(x, y):
    """
       Multiplies two numbers and returns the result.

       @param x: First number
       @param y: Second number
       @return: Product of x and y
       """
    return x * y

def divide(x, y):
    """
        Divides the first number by the second and returns the result.

        @param x: First number
        @param y: Second number
        @return: Quotient of x and y, or an error message if y is 0
        """
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

def calculator():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    while True:
        choice = input("Введите номер операции (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: введите числовое значение")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Хотите выполнить еще одну операцию? (да/нет): ")
            if next_calculation.lower() != 'да':
                break
        else:
            print("Неверный ввод. Пожалуйста, введите номер операции.")

if __name__ == "__main__":
    calculator()
