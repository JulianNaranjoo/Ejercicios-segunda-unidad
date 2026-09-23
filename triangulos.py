import math

def calcular_lal():
    a = float(input("Ingrese la longitud de a: "))
    angulo_c = float(input("Ingrese el angulo c: "))
    b = float(input("Ingrese la longitud de b: "))

    radianes_c = math.radians(angulo_c)

    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(radianes_c))

    sen_a = (a * math.sin(radianes_c)) / c
    radianes_a = math.asin(sen_a)
    angulo_a = math.degrees(radianes_a)

    angulo_b = 180.0 - angulo_a - angulo_c

    print(f"""Resultados:\n
    \rLado c: {c:.2f}
    \rAngulo de a: {angulo_a:.2f}°
    \rAngulo de b: {angulo_b:.2f}°""")

def calcular_ala():
    angulo_a = float(input("Ingrese el angulo de a: "))
    c = float(input("Ingrese longitud de c: "))
    angulo_b = float(input("Ingrese el angulo de b: "))
    
    angulo_c = 180.0 - angulo_a - angulo_b
    if angulo_c <= 0:
        print("Error, la suma de los angulos debe ser igual a 180°")
        return

    radianes_a = math.radians(angulo_a)
    radianes_b = math.radians(angulo_b)
    radianes_c = math.radians(angulo_c)

    a = (c * math.sin(radianes_a)) / math.sin(radianes_c)
    b = (c * math.sin(radianes_b)) / math.sin(radianes_c)

    print(f"""Resultados:\n
    \rLado a: {a:.2f}
    \rLado b: {b:.2f}
    \rAngulo de c: {angulo_c:.2f}°""")

def menu():
    opcion = int(input("""Seleccione el caso:\
        \r1- Lado-Ángulo-lado
        \r2- Ángulo-Lado-Ángulo
        opcion-->"""))

    if opcion == 1:
        calcular_lal()
    elif opcion == 2:
        calcular_ala()
    else:
        print("Ingrese una opción valida")

menu()


