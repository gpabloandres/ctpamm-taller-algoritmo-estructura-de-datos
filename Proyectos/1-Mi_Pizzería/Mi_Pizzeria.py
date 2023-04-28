# Declaración de las variables del programa
dinero = float(input("Hola, indique el dinero que lleva.\n"))
DINERO_INICIAL = dinero
total = 0
pedido = []

margarita = 7.85
jamon_queso = 9.65
cuatro_quesos = 8.95

extra_queso = 1.25
champinones = 0.85
albahaca = 0.5

# Título del programa
print("-> Pizzería PF <-\n")

# Bucle infinito (True) para pizzas - Número de ejecuciones indeterminadas
while True:
	# Menú de pizzas
    print(f"1 - Margarita - {margarita}$")
    print(f"2 - Jamón y queso - {jamon_queso}$")
    print(f"3 - Cuatro quesos - {cuatro_quesos}$")
    
	# Almacena la elección del usuario
    eleccion = int(input("Hola, por favor, seleccione su pizza con un número de opción.\n"))

    # Se calcula el cambio y el total, se indica la pizza elegida, se añade a la lista
    match eleccion:
        case 1:
            print(f"Ha elegido la pizza margarita.\nTotal a pagar {margarita}$.")
            dinero -= margarita
            print(f"Le quedan {round(dinero,2)}$.")
            total += margarita
            pedido.append(f"Margarita - {margarita}$")
            break
        case 2:
            print(f"Ha elegido la pizza de jamón y queso.\nTotal a pagar {jamon_queso}$.")
            dinero -= jamon_queso
            print(f"Le quedan {round(dinero,2)}$.")
            total += jamon_queso
            pedido.append(f"Jamón y queso - {jamon_queso}$")
            break
        case 3:
            print(f"Ha elegido la pizza cuatro quesos.\nTotal a pagar {cuatro_quesos}$.")
            dinero -= cuatro_quesos
            print(f"Le quedan {round(dinero,2)}$.")
            total += cuatro_quesos
            pedido.append(f"Cuatro quesos - {cuatro_quesos}$")
            break
        case _:
            print(f"Opción incorrecta. Seleccione una opción del 1 al 3.")

# Bucle infinito (True) para ingredientes - Número de ejecuciones indeterminadas            
while True:
	# Menú de ingredientes
    print(f"1 - Extra de queso - {extra_queso}$")
    print(f"2 - Champiñones - {champinones}$")
    print(f"3 - Albahaca - {albahaca}$")
    print(f"4 - No añadir nada extra y pagar.")
    
    # Almacena la elección del usuario
    eleccion = int(input("Si desea algún ingrediente extra, selecciónelo.\n"))
    
    # Se calcula el cambio y el total, se indican los ingredientes elegidos, 
    # se añaden a la lista...
    match eleccion:
        case 1:
            print(f"Ha elegido extra de queso.\nExtra a pagar {extra_queso}$.")
            dinero -= extra_queso
            total += extra_queso
            print(f"Total a pagar: {total}$.")
            print(f"Le quedan {round(dinero,2)}$.")
            pedido.append(f"Extra de queso - {extra_queso}$")
        case 2:
            print(f"Ha elegido champiñones extra.\nExtra a pagar {champinones}$.")
            dinero -= champinones
            total += champinones
            print(f"Total a pagar: {total}$.")
            print(f"Le quedan {round(dinero,2)}$.")
            pedido.append(f"Champiñones - {champinones}$")
        case 3:
            print(f"Ha elegido añadir albahaca.\nExtra a pagar {albahaca}$.")
            dinero -= albahaca
            total += albahaca
            print(f"Total a pagar: {total}$.")
            print(f"Le quedan {round(dinero,2)}$.")
            pedido.append(f"Albahaca - {albahaca}$")
        case 4:
            print("De acuerdo, no se añade nada extra.")
            break
        case _:
            print(f"Opción incorrecta. Seleccione una opción del 1 al 4.")

# Un condicional para determinar si le llega el dinero al usuario con su pedido.
# Si le llega, se ejecuta el if y le saca el ticket con todo lo pedido.
if total <= DINERO_INICIAL:
    print("\n--- SU PEDIDO ---")

    print(f"El total  de su pedido es: {total}$.")
    print(f"Su cambio: {dinero}$.\n")

    for i in pedido:
        print(f"-{i}.")

    print("\n¡Buen provecho!")

# Si el dinero no le llega, le indica que no le llega y no imprime el ticket.    
else:
    print("No le llega el dinero para todo eso. Por favor, vuelva a empezar.")