#----------------------------------------------------------
# Fecha: 12-04-23
# Estudiante: Su Nombre Completo
# Título: Bucles FOR y WHILE.
#----------------------------------------------------------

# Declarar y definir variables.
marcas = ["fiat", "ford", "vw", "chevrolet"] # esto es una lista de marcas

print("--LISTADO DE MARCAS---")

# print(colores)

# Bucle for para recorrer la lista de marcas.
print("Resultado del bucle for")
for marca in marcas:
    if marca == "fiat":
        continue
    print(f"-marca {marca}")

# Uso del bucle while.
# Variable para el bucle.
i = 1

print("Resultado del bucle while")
while i < 5:
    print(f"El valor del bucle es: {i}")
    i = i+1

