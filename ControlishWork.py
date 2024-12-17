def main(inp, a, b):
    def division(a,b):
        return a / b

    def multiplication(a,b):
        return a * b

    def subtraction(a, b):
        return a - b

    def summ(a, b):
        return a + b

    def pow(a, b):
        return a ** b

    def S(a, b):
        return a * b

    def P(a, b):
        return (a + b) * 2

    if inp == "+":
        return summ(a,b)
    elif inp == "-":
        return subtraction(a,b)
    elif inp == "*":
        return multiplication(a,b)
    elif inp == "/":
        return division(a,b)
    elif inp == "^":
        return pow(a,b)
    elif inp == "S":
        return S(a,b)
    elif inp == "P":
        return P(a,b)

while 1:
    try:
        print("\nДобро пожаловать в калькулятор!") #Вывод приветсвия
        print("'+', '-', '/', '*', '^', 'S', 'P',") #Список операция
        inp = str(input("Выберите операцию из выше перечисленных: ")) #Выбор операции

        if(inp != "+" and inp != "-" and inp != "/" and inp != "*" and inp != "^" and inp != "S" and inp != "P"): #Проверка выбора операции
            print("ОТВЕТ НЕВЕРНЫЙ! ПОПРОБУЙТЕ ЕЩЁ РАЗ.") #Говорим что так нельзя
            passs = input("Нажмите ENTER чтобы продолжить...") #Ждём обратной связи от юзера
            continue

        num1 = int(input("Введите первое число: ")) #Введите первое число
        num2 = int(input("Введите второе число: ")) #Введите второе число
        print(main(inp, num1, num2)) #Считаем...
        passs = input("Нажмите ENTER чтобы продолжить...") #Ждём обратной связи от юзера

    except ValueError:
        print("Ошибка")
        passs = input("Нажмите ENTER чтобы продолжить...")  # Ждём обратной связи от юзера
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        passs = input("Нажмите ENTER чтобы продолжить...")  # Ждём обратной связи от юзера
    except TypeError:
        print("Ошибка")
        passs = input("Нажмите ENTER чтобы продолжить...") #Ждём обратной связи от юзера