def total_sum(array):
    total = 0
    for i in array:
        total += i
    return total

def total_avg(array):
    total = 0
    count = 0
    for i in array:
        total += i
        count += 1
    avg = total / count
    return avg

def positive_negative(array):
    positive = 0
    negative = 0
    for i in array:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
    return positive, negative

def area_triangle(base, height):
    area = (base * height) / 2
    return area

def even(num):
    return num % 2 == 0

def max_min(array):
    maximum = max(array)
    minimum = min(array)
    return maximum, minimum

while True:
    print("\n--------Bienvenido al programa----------\n1. obtener sumatoria, promedio y cantidad de positivos y negativos de una serie numérica\n2. calcular el área de un triángulo\n3. verificar si un número es par o impar\n4. calcular promedio de calificaciones\n5. mostrar el mayor y el menor de una serie numérica\n6. salir")
    option = input("Seleccione una opción: ")
    match option:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            print("Saliendo...")
            break
        case _:
            print("Elija una opción válida")





