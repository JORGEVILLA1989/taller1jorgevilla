frutas = []
total_costo = 0

n = int(input("Ingrese la cantidad de frutas: "))
for i in range(n):
    id_fruta = i + 1
    nombre_fruta = input(f"Digite el nombre de la fruta {id_fruta}: ")
    precio_unitario_fruta = float(input(f"Digite el valor de la {nombre_fruta}: "))
    cantidad_fruta = int(input(f"Digite la cantidad de la {nombre_fruta}: "))
    frutas.append({'id': id_fruta, 'nombre': nombre_fruta, 'precio_unitario': precio_unitario_fruta, 'cantidad': cantidad_fruta})


costo_total = sum(fruta['precio_unitario'] * fruta['cantidad'] 
for fruta in frutas)
print("El costo total del salpicón es:", costo_total)


fruta_mas_barata = min(frutas, key=lambda x: x['precio_unitario'])
print("La fruta más barata es:", fruta_mas_barata['nombre'], ", Precio:", fruta_mas_barata['precio_unitario'])

frutas_ordenadas = sorted(frutas, key=lambda x: x['precio_unitario'], reverse=True)
print("Frutas ordenadas por costo:")
for fruta in frutas_ordenadas:
    print("Fruta:", fruta['nombre'], ", Precio:", fruta['precio_unitario'], ", Cantidad:", fruta['cantidad'])

