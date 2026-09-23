from datetime import datetime

base_de_datos = []

def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year
    cumplio = (hoy.month, hoy.day) >= (fecha_nacimiento.month, fecha_nacimiento.day)
    if not cumplio:
        edad -= 1
    return edad

def crear_paciente():
    print("Registro de nuevo paciente")
    nombre = input("Ingrese el nombre del paciente: ")
    documento = input("Ingrese el documento del paciente: ")

    while True:
        try:
            fecha = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
            fecha_nacimiento = datetime.strptime(fecha, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha inválido")

    edad = calcular_edad(fecha_nacimiento)
    eps = input("Ingrese la EPS: ")

    paciente = (nombre, documento, fecha_nacimiento, edad, eps)
    return paciente

def guardar_paciente(bd, paciente):
    bd.append(paciente)
    print("Paciente guardado exitosamente.")

def buscar_paciente(bd):
    print("---Busaqueda de paciente---")
    id = input("Ingrese el documento del paciente: ")
    identificacion = [paciente[1] for paciente in bd]

    if id in identificacion:
        for paciente in bd:
            if paciente[1] == id:
                nombre, doc, f_nac, edad, eps = paciente
                print(f"""Paciente encontrado\n
                \rNombre: {nombre}
                \rDocumento: {doc}
                \rFecha de nacimiento: {f_nac}
                \rEdad: {edad}
                \rEps: {eps}""")
                break
            else:
                print("Paciente no encontrado")


def mostrar_todos(bd):
    print("Base de datos de la historia clinica")

    if not bd:
        print("No hay pacientes registrados")
    else:
        for i, paciente in enumerate(bd,1):
            nombre, doc, f_nac, edad, eps = paciente
            print(f"""paciente #{i}:
            \rNombre: {nombre}
            \rDocumento: {doc}
            \rFecha de nacimiento: {f_nac.strftime('%d/%m/%Y')}
            \rEdad: {edad}
            \rEPS: {eps}""")

def menu():
    while True:
        opcion = int(input("""---MENU PRINCIPAL---\n
        \r1.Ingresar un nuevo paciente
        \r2.Buscar un paciente
        \r3.Salir"""))

        if opcion == 1:
            nuevo_paciente = crear_paciente()
            guardar_paciente(base_de_datos, nuevo_paciente)
        elif opcion == 2:
            buscar_paciente(base_de_datos)
        elif opcion == 3:
            print("Sliendo del sistema")
            mostrar_todos(base_de_datos)
            break
        else:
            print("Ingrese una opcion valida")

menu()