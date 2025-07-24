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
            array_1 = []
            while True:
                try:
                    length_array = int(input("¿Cuántos números va a ingresar?: "))
                    if length_array <= 0:
                        print("Debe ser un número positivo")
                    else:
                        break
                except:
                    print("Ingrese un número entero")

            for i in range(length_array):
                while True:
                    try:
                        val = int(input(f"Ingrese el valor {i+1}: "))
                        array_1.append(val)
                        break
                    except:
                        print("Debe ingresar un número entero")

            first_sum = total_sum(array_1)
            first_avg = total_avg(array_1)
            first_positive, first_negative = positive_negative(array_1)
            print(f"La suma de los valores es: {first_sum}")
            print(f"El promedio de los valores es: {first_avg}")
            print(f"La cantidad de valores positivos es: {first_positive}")
            print(f"La cantidad de valores negativos es: {first_negative}")


        case "2":
            while True:
                try:
                    base = int(input("Ingrese la medida de la base del triángulo: "))
                    height = int(input("Ingrese la altura del triángulo: "))
                    if base<0 or height<0:
                        print("\nSolo ingrese valores positivos")
                    else:
                        break
                except:
                    print("\nIngrese números enteros")

            print("El área del triángulo es: " + area_triangle(base, height))


        case "3":
            while True:
                try:
                    val = int(input("Ingrese un número: "))
                    break
                except:
                    print("\nIngrese números enteros")

            confirm = even(val)
            if confirm:
                print("El número es par")
            else:
                print("El número es impar")


        case "4":
            array_2 = []
            while True:
                try:
                    length_array2 = int(input("¿Cuántas notas va a ingresar?: "))
                    if length_array2 <= 0:
                        print("Debe ser un número positivo")
                    else:
                        break
                except:
                    print("Ingrese un número entero")

            for i in range(length_array2):
                while True:
                    try:
                        nota = int(input(f"Ingrese la nota {i+1}: "))
                        if nota > 0 and nota < 100:
                            array_2.append(nota)
                            break
                        else:
                            print("La nota debe ser positiva y no mayor a 100")
                    except:
                        print("Ingrese un número entero")
                print("El promedio de todas las notas es de: " + total_avg(array_2))


        case "5":
            pass
        case "6":
            print("Saliendo...")
            break
        case _:
            print("Elija una opción válida")





