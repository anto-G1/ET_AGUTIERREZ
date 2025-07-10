
# Diccionarios iniciales
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2060Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}
# Se genera una lista con el stock de cada producto
stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1]
}

# Función 1
def stock_marca(marca):
    total = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca.lower():
            total += stock[modelo][1]
    print("Stock total para marca", marca.upper(), ":", total)

# Función 2
def busqueda_precio(p_min, p_max):
    try:
        encontrados = []
        for modelo in stock:
            precio = stock[modelo][0]
            cantidad = stock[modelo][1]
            if p_min <= precio <= p_max and cantidad > 0:
                encontrados.append(modelo)
        if len(encontrados) == 0:
            print("No hay notebooks en ese rango de precios, vuelve a intentarlo.")
        else:
            encontrados.sort()
            print("Modelos encontrados:")
            for m in encontrados:
                print(m)
    except:
        print("Debe ingresar valores válidos.")

# Función 3
def eliminar_producto(modelo):
    if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock[modelo]
        print("Producto eliminado!!")
        return True
    else:
        print("El modelo no existe!!")
        return False

# Programa principal
def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca")
        print("2. Búsqueda por precio")
        print("3. Eliminar producto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            marca = input("Ingrese la marca: ")
            stock_marca(marca)

        elif opcion == "2":
            try:
                p_min = int(input("Precio mínimo: "))
                p_max = int(input("Precio máximo: "))
                busqueda_precio(p_min, p_max)
            except:
                print("Debe ingresar valores válidos (números enteros).") #para manero de errores se pide al usuario ingresar numeros, en caso de ingresar un caracter no válido.

        elif opcion == "3":
            modelo = input("Ingrese el modelo a eliminar: ")
            resultado = eliminar_producto(modelo)
            if resultado:
                decision = input("¿Desea eliminar otro producto? (si/no): ")        #Se da la opción al usuario de volve a eliminar productos
                if decision.lower() != "si":
                    continue
            else:
                continue

        elif opcion == "4":
            print("Programa finalizado con éxito.")
            break

        else:
            print("Debe seleccionar una opción válida!!")
menu()