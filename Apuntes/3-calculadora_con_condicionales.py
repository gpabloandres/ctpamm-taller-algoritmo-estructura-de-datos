#--------------------------------------------------------------------------------------------
# Fecha: 10-04-23
# Estudiante: Su Nombre Completo
# Título: Calculadora Básica usando condicional if-else.
# Documentación: Ingresar 2 números aleatorios y elegir una operación matemática para ellos.
#--------------------------------------------------------------------------------------------

# Declarar y definir las variables.

numero_1 = float(input("Introduce el valor del primer número: "))
numero_2 = float(input("Introduce el valor del segundo número: "))

# Empezar con el cálculo

print("¿Qué operación desea realizar?")

# Presentar menú de opciones.

print("1. Sumar")

print("2. Restar")

print("3. Multiplicar")

print("4. Dividir")

# Guardar en una variable la opción seleccionada. 

operacion = input("Ingrese su opción: ")

# Procesar la opción seleccionada.

if operacion =="1":
    print("La suma de ambos números es igual a: ")
    print(numero_1 + numero_2)

elif operacion =="2":
    print("La resta de ambos números es igual a: ")
    print(numero_1 - numero_2)

elif operacion =="3":
    print("La multiplicación de ambos números es igual a: ")
    print(numero_1 * numero_2)

elif operacion =="4":
    # Evito dividir por cero.
    if numero_2 == 0:
        print("Operación inválida")
    else:
        print("La división de ambos números es igual a: ")
        print(numero_1 / numero_2)

else:
    print("Opción inválida, vuelva a intentarlo.")

# Fin del programa.