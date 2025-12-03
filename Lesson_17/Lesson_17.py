x = int(input("Введите число: "))

if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

x = int(input("Введите целое число: "))

if x % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")




    x = float(input("Введите число: "))

    if 1 <= x <= 10:
        print("Число в диапазоне")
    else:
        print("Число вне диапазона")

        a = float(input("Введите a: "))
        b = float(input("Введите b: "))

        if a < b:
            a, b = b, a

        print(a, b)

        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))

        print("Минимальное число:", min(a, b))

        x = int(input("Введите число: "))

        if x % 3 == 0 and x % 5 == 0:
            print("Число делится на 3 и 5")
        elif x % 3 == 0:
            print("Число делится только на 3")
        elif x % 5 == 0:
            print("Число делится только на 5")
        else:
            print("Число не делится на 3 и 5")

            password = input("Введите пароль: ")

            if password == "admin123":
                print("Доступ разрешен")
            else:
                print("Доступ запрещен")