print("Hola, bienvenido a nuestro servicio de Uber")
nombre = input("Para continuar, por favor escribe tu nombre: ")
print("Hola " + nombre)
print("Para continuar, elige alguno de nuestros productos")

while True:
    # Opciones de comida
    print("\n**** COMIDA DISPONIBLE ****")
    print("1 - HAMBURGUESAS")
    print("2 - PIZZA")
    print("3 - TACOS")
    print("4 - SUSHI")
    print("5 - POLLO")
    comida = int(input("Por favor elige alguna de las siguientes opciones (1-5): "))

    # Opciones de restaurantes y menú de comida
    if comida == 1:
        # HAMBURGUESAS
        print("\n**** RESTAURANTES DE HAMBURGUESAS ****")
        print("1 - McDonald's")
        print("2 - Burger King")
        print("3 - Carl's Jr")
        restaurante = int(input("Por favor elige alguno de nuestros restaurantes disponibles: "))

        if restaurante == 1:
            print("\nBienvenido a nuestro catálogo de McDonald's")
            print("Elige alguna de las siguientes opciones:")
            print("1 - Big Mac ($126)")
            print("2 - Cajita Feliz ($139)")
            print("3 - Mc Crispy ($195)")
            opcion = int(input("Elige una opción de comida (1-3): "))
            if opcion == 1:
                comida_seleccionada, precio_comida = "Big Mac", 126
            elif opcion == 2:
                comida_seleccionada, precio_comida = "Cajita Feliz", 139
            elif opcion == 3:
                comida_seleccionada, precio_comida = "Mc Crispy", 195
            else:
                print("Opción inválida. Volviendo al menú principal.")
                continue

        elif restaurante == 2:
            print("\nBienvenido a nuestro catálogo de Burger King")
            print("Elige alguna de las siguientes opciones:")
            print("1 - Whopper ($130)")
            print("2 - King de Pollo ($140)")
            print("3 - King Jr ($90)")
            opcion = int(input("Elige una opción de comida (1-3): "))
            if opcion == 1:
                comida_seleccionada, precio_comida = "Whopper", 130
            elif opcion == 2:
                comida_seleccionada, precio_comida = "King de Pollo", 140
            elif opcion == 3:
                comida_seleccionada, precio_comida = "King Jr", 90
            else:
                print("Opción inválida. Volviendo al menú principal.")
                continue

        elif restaurante == 3:
            print("\nBienvenido a nuestro catálogo de Carl's Jr")
            print("Elige alguna de las siguientes opciones:")
            print("1 - Famous Star ($150)")
            print("2 - Super Star ($160)")
            print("3 - Western Bacon ($170)")
            opcion = int(input("Elige una opción de comida (1-3): "))
            if opcion == 1:
                comida_seleccionada, precio_comida = "Famous Star", 150
            elif opcion == 2:
                comida_seleccionada, precio_comida = "Super Star", 160
            elif opcion == 3:
                comida_seleccionada, precio_comida = "Western Bacon", 170
            else:
                print("Opción inválida. Volviendo al menú principal.")
                continue
        else:
            print("Opción inválida. Volviendo al menú principal.")
            continue

    elif comida == 2:
        # PIZZA
        print("\n**** RESTAURANTES DE PIZZA ****")
        print("1 - Domino's")
        print("2 - Little Caesars")
        print("3 - Papa John's")
        restaurante = int(input("Por favor elige alguno de nuestros restaurantes disponibles: "))

        if restaurante == 1:
            print("\nBienvenido a nuestro catálogo de Domino's")
            print("Elige alguna de las siguientes opciones:")
            print("1 - Pepperoni ($90)")
            print("2 - Hawaiana ($85)")
            print("3 - Cuatro Quesos ($100)")
            opcion = int(input("Elige una opción de comida (1-3): "))
            if opcion == 1:
                comida_seleccionada, precio_comida = "Pepperoni", 90
            elif opcion == 2:
                comida_seleccionada, precio_comida = "Hawaiana", 85
            elif opcion == 3:
                comida_seleccionada, precio_comida = "Cuatro Quesos", 100
            else:
                print("Opción inválida. Volviendo al menú principal.")
                continue

    elif comida == 3:
        # TACOS
        print("\n**** RESTAURANTES DE TACOS ****")
        print("1 - Taco Bell")
        print("2 - El Fogoncito")
        print("3 - Taquería Doña Lupita")
        restaurante = int(input("Por favor elige alguno de nuestros restaurantes disponibles: "))

        if restaurante == 1:
            print("\nBienvenido a nuestro catálogo de Taco Bell")
            print("Elige alguna de las siguientes opciones:")
            print("1 - Taco Supreme ($40)")
            print("2 - Quesadilla ($50)")
            print("3 - Burrito ($45)")
            opcion = int(input("Elige una opción de comida (1-3): "))
            if opcion == 1:
                comida_seleccionada, precio_comida = "Taco Supreme", 40
            elif opcion == 2:
                comida_seleccionada, precio_comida = "Quesadilla", 50
            elif opcion == 3:
                comida_seleccionada, precio_comida = "Burrito", 45
            else:
                print("Opción inválida. Volviendo al menú principal.")
                continue

    elif comida == 4:
        # SUSHI
        print("\n**** RESTAURANTES DE SUSHI ****")
        print("1 - Sushi Itto")
        print("2 - Sushin' Go")
        print("3 - Sushi Roll")
        restaurante = int(input("Por favor elige alguno de nuestros restaurantes disponibles: "))

        if restaurante == 1:
            print("\nBienvenido a nuestro catálogo de Sushi Itto")
            print("Elige alguna de las siguientes opciones:")
            print("1 - California Roll ($60)")
            print("2 - Spicy Tuna ($70)")
            print("3 - Ebi Tempura ($75)")
            opcion = int(input("Elige una opción de comida (1-3): "))
            if opcion == 1:
                comida_seleccionada, precio_comida = "California Roll", 60
            elif opcion == 2:
                comida_seleccionada, precio_comida = "Spicy Tuna", 70
            elif opcion == 3:
                comida_seleccionada, precio_comida = "Ebi Tempura", 75
            else:
                print("Opción inválida. Volviendo al menú principal.")
                continue

    elif comida == 5:
        # POLLO
        print("\n**** RESTAURANTES DE POLLO ****")
        print("1 - KFC")
        print("2 - Pollo Campero")
        print("3 - Church's Chicken")
        restaurante = int(input("Por favor elige alguno de nuestros restaurantes disponibles: "))

        if restaurante == 1:
            print("\nBienvenido a nuestro catálogo de KFC")
            print("Elige alguna de las siguientes opciones:")
            print("1 - Chicken Bucket ($150)")
            print("2 - Crispy Strips ($80)")
            print("3 - Chicken Sandwich ($60)")
            opcion = int(input("Elige una opción de comida (1-3): "))
            if opcion == 1:
                comida_seleccionada, precio_comida = "Chicken Bucket", 150
            elif opcion == 2:
                comida_seleccionada, precio_comida = "Crispy Strips", 80
            elif opcion == 3:
                comida_seleccionada, precio_comida = "Chicken Sandwich", 60
            else:
                print("Opción inválida. Volviendo al menú principal.")
                continue

    else:
        print("Opción inválida. Volviendo al menú principal.")
        continue

    # Opciones de condimentos adicionales
    print("\nOpciones de condimentos:")
    print("1 - Queso extra (+$10)")
    print("2 - Salsa BBQ (+$5)")
    print("3 - Papas fritas (+$15)")
    cond_choice = int(input("Elige un condimento adicional (1-3) o 0 para ninguno: "))
    if cond_choice == 0:
        condimento_seleccionado, precio_condimento = "Ninguno", 0
    elif cond_choice == 1:
        condimento_seleccionado, precio_condimento = "Queso extra", 10
    elif cond_choice == 2:
        condimento_seleccionado, precio_condimento = "Salsa BBQ", 5
    elif cond_choice == 3:
        condimento_seleccionado, precio_condimento = "Papas fritas", 15
    else:
        print("Opción inválida")