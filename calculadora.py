def suma (x,y):
    return x + y
def resta (x,y):
    return x - y
def multiplicacion (x,y):
    return x * y
def division (x,y):
    if y == 0:
        return "Error, no se puede dividir entre 0"
    return x / y

def calculadora():
    while True:
        opcion = int(input("""MENU:\n
        \r1-Suma
        \r2-Resta
        \r3-Multiplicación
        \r4-División
        \r5-Salir
        opción-->"""))

        if opcion == 5:
            print("¡Hasta luego!")
            break

        if opcion in (1,2,3,4):
            numero_1 = float(input("Ingrese el primer número:"))
            numero_2 = float(input("Ingrese el segundo número:"))
        else:
            print("Ingrese una opción valida")
            continue

        if opcion == 1:
            print(f"Resiltado: {suma(numero_1,numero_2)}")
        elif opcion == 2:
            print(f"Resultado: {resta(numero_1,numero_2)}")
        elif opcion == 3:
            print(f"Resiultado: {multiplicacion(numero_1,numero_2)}")
        elif opcion == 4:
            print(f"Resultado: {division(numero_1,numero_2)}")

calculadora()        