print("Hola, para continuar ingresa tu nombre por favor")
N = input("Ingresa tu nombre: ")

print("Bienvenido a nuestra terminal, " + N + "!")

# Iniciar ciclo para la selección de vuelos
while True:
    # Elección de vuelo
    print("** VUELOS DISPONIBLES **")
    print(N + ", presiona 1 para elegir el viaje a Nueva Zelanda")
    print(N + ", presiona 2 para elegir el viaje a Estados Unidos")
    print(N + ", presiona 3 para elegir el viaje a Alemania")
    print(N + ", presiona 4 para elegir el viaje a Japón")
    print(N + ", presiona 5 para elegir el viaje a Reino Unido")

    op = int(input("Por favor elige el vuelo que desees (1-5): "))

    # Procesar la opción de vuelo
    if op == 1:
        destino = "Nueva Zelanda"
        precio_adulto = 800
        precio_nino = 500
        precio_bebe = 200
    elif op == 2:
        destino = "Estados Unidos"
        precio_adulto = 600
        precio_nino = 400
        precio_bebe = 150
    elif op == 3:
        destino = "Alemania"
        precio_adulto = 700
        precio_nino = 450
        precio_bebe = 180
    elif op == 4:
        destino = "Japón"
        precio_adulto = 900
        precio_nino = 550
        precio_bebe = 220
    elif op == 5:
        destino = "Reino Unido"
        precio_adulto = 750
        precio_nino = 480
        precio_bebe = 170
    else:
        print("Opción no válida. Reinicia el programa.")
        continue

    # Solicitar cantidad de boletos
    print("Elección: Boleto a " + destino + ".")
    BA = int(input("Elige cuántos boletos para ADULTOS (+14): "))
    BN = int(input("Elige cuántos boletos para NIÑOS (2-13): "))
    Bb = int(input("Elige cuántos boletos para BEBÉS (<2): "))

    # Mostrar resumen de selección
    print("Haz seleccionado " + str(BA) + " boletos de adulto, " + str(BN) + " boletos de niño y " + str(Bb) + " boletos para bebé.")

    # Calcular el costo total
    total = (BA * precio_adulto) + (BN * precio_nino) + (Bb * precio_bebe)

    print("El costo total para tu vuelo a " + destino + " es: $" + str(total))
    print("A continuación, elige las opciones de equipaje disponibles:")
    print("1 mochila: $20 cada una")
    print("2 bolsas: $10 cada una")
    print("3 maletas: $30 cada una")
    
    mochilas = int(input("¿Cuántas mochilas deseas llevar? "))
    bolsas = int(input("¿Cuántas bolsas deseas llevar? "))
    maletas = int(input("¿Cuántas maletas deseas llevar? "))

    # Cálculo del costo del equipaje
    costo_equipaje = (mochilas * 20) + (bolsas * 10) + (maletas * 30)

    # Descuento opcional
    descuento = input("¿Aplicas algún descuento (estudiante/amex)? Si no, presiona Enter: ").lower()

    if descuento == "estudiante":
        total *= 0.90  # 10% de descuento
        print("Se ha aplicado un descuento de estudiante. El nuevo total es: $" + str(total))
    elif descuento == "amex":
        total *= 0.85  # 15% de descuento
        print("Se ha aplicado un descuento por American Express. El nuevo total es: $" + str(total))
    else:
        print("sin descuento.")

    # Preguntar si desea continuar con la compra o regresar
    continuar = input("¿Deseas continuar con este vuelo (sí/no) o regresar a elegir otro destino (regresar)? ").lower()

    if continuar == "sí" or continuar == "si":
        print("Gracias por tu compra, " + N + "! Tu vuelo a " + destino + " está confirmado.")
        break  # Finaliza el ciclo si elige continuar
    elif continuar == "no":
        print("Has cancelado tu compra.")
        break  # Finaliza el ciclo si elige no continuar
    elif continuar == "regresar":
        print("Regresando a la selección de destinos...")
        continue  # Vuelve a empezar el ciclo si desea regresar a la elección del destino
    else:
        print("Opción no válida. Volviendo a la elección del destino.")
        continue
    