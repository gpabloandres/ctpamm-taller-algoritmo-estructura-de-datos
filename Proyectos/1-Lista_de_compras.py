#------------------------------------------------------------------------------------
# Fecha: 19-04-23
# Estudiante: Su nombre
# Título: Proyecto 1 -Lista de Compras
#------------------------------------------------------------------------------------

# importar bibliotecas
import os

# Definir y declarar variables
# Crear una lista vacia
lista_articulos = list()

while True:
    print("Menú")
    print("1.- Agregar artículos")
    print("2.- Borrar artículos")
    print("3.- Ver lista de artículos")
    print("4.- Salir")
    
    opcion = int(input("¿Qué desea hacer?: "))
    
    # si no es ninguna de las 4 opciones validas
    if opcion <= 0 or opcion > 4:
        print("Favor de ingresar una opcion valida")
        continue
    elif opcion == 1:
        # Agregar artículos a la lista.
        print()
        print("Favor agregar tus artículos")
        print()
        articulos = input("Agrega tu artículo: ")
        lista_articulos.append(articulo)
        print("Articulo agregado")
        print()
    elif opcion == 2:
        # Borrar elementos de la lista.
        articulo = input("Elementos a eliminar: ")
        lista_articulos.remove(articulo)
        print("¡El artículo se ha borrado con éxito!")
    elif opcion == 3:
        # Imprimir los artículos de la lista.            
        print()
        print("Artículos en tu lista")
        print()
        for articulos in lista_articulos:
            print()
            print(articulos)
            print()
        print("Estos son tus artículos: ")
    else:
        break
print("Gracias por utilizar la lista hecha en Python")