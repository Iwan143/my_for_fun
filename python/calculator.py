def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Ошибка, деление на ноль"
    return x / y

def calc():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычетание")
    print("3. Умножение")
    print("4. Деление")

    ch = input("Введите номер операции (1/2/3/4): ")

    if ch in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка, введите числовое значение")
            return

        if ch == '1':
            print(f"Результат: {add(num1, num2)}") 
        elif ch == '2':
            print(f"Результат: {sub(num1, num2)}") 
        elif ch == '3':
            print(f"Результат: {mul(num1, num2)}")            
        elif ch == '4':
            print(f"Результат: {div(num1, num2)}")   
    else:
        print("Неверный выбор операции")

if __name__ == "__main__":
    calc()                 