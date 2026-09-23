def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

def dias_del_mes(mes, año):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if bisiesto(año):
            return 29
        else:
            return 28
    return 0

def calcular_dia_sig(dia, mes, año):
    max_dias = dias_del_mes(mes, año)
    if dia == max_dias:
        dia_sig = 1
        if mes == 12:
            mes_sig = 1
            año_sig = año + 1
        else:
            mes_sig = mes + 1
            año_sig = año
    else:
        dia_sig = dia + 1
        mes_sig = mes
        año_sig = año

    return dia_sig, mes_sig, año_sig

def fecha_valida(dia, mes, año):
    if mes < 1 or mes > 12:
        return False
    max_dias = dias_del_mes(mes, año)
    if dia < 1 or dia > max_dias:
        return False
    return True

def programa():
    while True:
        print("CALCULO DEL DÍA SIGUIENTE".center(90))
        try:
            dia = int(input("Ingrese el dia (dd): "))
            mes = int(input("Ingrese el mes (mm): "))
            año = int(input("Ingrese el año (aaaa): "))

            if not fecha_valida(dia, mes, año):
                print("Error: Fecha invalida")
                continue

            dia_sig, mes_sig, año_sig = calcular_dia_sig(dia, mes, año)
            print(f"Fecha ingresada: {dia:02d}/{mes:02d}/{año}")
            print(f"Fecha del dia siguiente: {dia_sig:02d}/{mes_sig:02d}/{año_sig}")
        except ValueError:
            print("Error, ingrese valores validos")
            continue

        opcion = int(input("Ingrese 0-Si desea salir, 1-Si desea ingresar otra fecha"))
        if opcion == 0:
            break
        elif opcion == 1:
            continue
        else:
            print("Ingrese una opcion valida")

programa()