camisetas = {1:['polo', 'blanca', 15], 2:['polo', 'azul', 15], 3:['polo', 'roja', 15], 5:['polo', 'amarilla', 15], 6:['cuello redondo', 'gris', 12], 7:['cuello redondo', 'negro', 12], 8:['cuello redondo', 'verde', 12]}
jeans = {1:['azul', 20], 2:['verde', 20], 3:['cafe', 20], 4:['negro', 20], 5:['gris', 20]}
zapatos = {1:['botas', 'cafe', 25], 2:['tenis', 'azul', 20], 3:['botas', 'negro', 25], 4:['tenis', 'blanco', 20]}

def ingreso_num(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Ingrese solo numeros")

def opcion_dic(diccio, categoria):
    while True:
        print(f"\nCatalogo de {categoria}\n".center(90))
        for clave, valor in diccio.items():
            print(f"{clave}. {valor}")

        opcion = ingreso_num(f"Seleccione el número correspondiente a {categoria}: ")
        if opcion in diccio:
            return diccio[opcion]
        else:
            print("Opcion invalida, el número ingresado no esta en el catalogo")

def reliz_compra():
    while True:
        print("\nDatos del comprador\n".center(90))
        nombre = input("Ingrese el nombre y apellidos: ")
        documento = ingreso_num("Ingrese el número de documento: ")
        direccion = input("Ingrese la dirección: ")
        telefono = ingreso_num("Ingrese número de telefono: ")

        compra = []

        print("\nSeleccion de articulos\n".center(90))

        art_1 = opcion_dic(camisetas, "Camisetas")
        compra.append(["Camisetas", art_1])

        art_2 = opcion_dic(jeans, "Jeans")
        compra.append(["Jean", art_2])

        art_3 = opcion_dic(zapatos, "Zapatos")
        compra.append(["Zapato", art_3])

        total_compra = 0
        print(f"""RESUMEN DE COMPRA\n
        \rCliente: {nombre}
        \rDocumento: {documento}
        \rDirección: {direccion}
        \rTelefono: {telefono}""")

        print("\nARTICULOS:")
        for i, item in enumerate(compra, 1):
            tipo = item[0]
            detalles = item[1]
            precio = detalles[-1]

            descripcion = "-".join(str(d) for d in detalles[:-1])
            print(f"{i}. {tipo} ({descripcion})-->${precio}")
            total_compra += precio

            print(f"VALOR TOTAL: ${total_compra}\n")

        opcion_otra_com = int(input("Ingrese:\n1-Si desea hacer otra compra.\n2-Si desea salir\n"))
        if opcion_otra_com == 2:
            print("Gracias por su compra")
            break
        


reliz_compra()