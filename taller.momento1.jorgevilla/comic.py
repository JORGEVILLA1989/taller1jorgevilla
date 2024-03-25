productos = []
opcion = 10

while opcion != 5:
    print("********* Tienda del cómic ********")
    print("********* Menú de opciones *******")
    print("1. Registrar producto")
    print("2. Mostrar inventario de la tienda")
    print("3. Buscar producto por nombre")
    print("4. Modificar producto")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1: 
        print("Registrar producto")
        import random
        
        producto = {}
        producto["id"] = random.randint(1, 100)
        print("ID del producto:", producto["id"])
        producto["Nombre"] = input("Nombre del producto a registrar: ")
        producto["Precio"] = float(input("Digite el precio de producto: "))
        producto["Ubicacion"] = input("Digite la ubicación del producto en la tienda (A,B,C o D): ")
        producto["Referencia"] = input("Digite la referencia del producto: ")
        producto["Pais de origen"] = input("País de origen del producto: ")
        producto["Unidades"] = input("Unidades compradas: ")
        producto["Garantia"] = input("¿Tiene garantía el producto? (true/false): ")
        productos.append(producto)
        

    elif opcion == 2:
        print("Mostrar  inventario de la tienda")
        for producto in productos:
            print(f"Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Ubicación: {producto['Ubicacion']}, Referencia: {producto['Referencia']}, País de origen: {producto['Pais de origen']}, Unidades: {producto['Unidades']}, Garantía: {producto['Garantia']}")

    elif opcion == 3:
        buscar_producto = input("Digite el nombre del producto: ")
        encontrado = False  
        for producto in productos:
            if producto["Nombre"] == buscar_producto:
                encontrado = True
                print("Lo encontré")
                break  
        if not encontrado:
            print("No lo encontré")


    elif opcion == 4:
     print("Modificar producto")
    modificar_producto = input("Ingrese el nombre del producto que desea modificar: ")
    encontrado = False
    
    for producto in productos:
        if producto["Nombre"] == modificar_producto:
            encontrado = True
            print("Producto encontrado. Proporcione los nuevos valores:")
            producto["Precio"] = float(input(f"Nuevo precio para '{producto['Nombre']}': "))
            producto["Ubicacion"] = input(f"Nueva ubicación para '{producto['Nombre']}': ")
            producto["Referencia"] = input(f"Nueva referencia para '{producto['Nombre']}': ")
            producto["Pais de origen"] = input(f"Nuevo país de origen para '{producto['Nombre']}': ")
            producto["Unidades"] = input(f"Nuevas unidades para '{producto['Nombre']}': ")
            producto["Garantia"] = input(f"¿Nuevo estado de garantía para '{producto['Nombre']}' (true/false): ")
            print("Producto modificado correctamente.")
            break
            
    if not encontrado:
        print("El producto no fue encontrado.")


    elif opcion == 5:
        print("Salio del programa")
        break
    else:
        print("Opcion invalida, seleccione una opcion valida")

    
        
     



    
    