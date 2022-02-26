#Реализовать функцию my_func(), которая принимает три позиционных
#аргумента, и возвращает сумму наибольших двух аргументов.

def fun(x, y, z):
    suma = [x, y, z]
    total = []
    a = max(suma)
    total.append(a)
    suma.remove(a)
    b = max(suma)
    total.append(b)

    print(sum(total))
print(fun(int(input("Введите первое число:")), int(input("Введите второе число: ")), int(input("Введите третье число:"))))