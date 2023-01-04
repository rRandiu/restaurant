############################
#           IDK            #
############################
equalbar = "|=============================|"
leavebar = "| J |========= SALIR =========|"
invalid = [equalbar, "|     Seleccion Invalida!     |", equalbar]
invalid1 = len(invalid)


def solicitar_cantidad():
    try:
        return int(input("Cuantos desea?: "))
    except ValueError:
        for invalid1 in invalid:
            print(invalid1)
        return solicitar_cantidad()


############################
#      Menu Selection      #
############################
selec1 = [equalbar, "|        RESTAURANTE S.A      |", "|            MENÚ             |", equalbar,
                    "| A |Desayuno                 |", "| B |Almuerzo                 |",
                    "| C |Cena                     |", "| D |========= PAGAR =========|", equalbar]
list1 = len(selec1)

############################
#          Menus           #
############################
desayuno = [equalbar, "| A |Café             |S/4.50 |", "| B |Chocolate        |S/5.00 |",
                      "| C |Jugo de Fresas   |S/9.00 |", "| D |Jugo de Papaya   |S/8.00 |",
                      "| E |Pan con Pollo    |S/7.00 |", "| F |Pan con Jamón    |S/7.00 |",
                      "| G |Pan con Tortilla |S/7.00 |", "| H |=== Lista de pedidos  ===|", leavebar, equalbar]
list2 = len(desayuno)

almuerzo = [equalbar, "| A |Café             |S/4.50 |", "| B |Chocolate        |S/5.00 |",
                      "| C |Jugo de Fresas   |S/9.00 |", "| D |Jugo de Papaya   |S/8.00 |",
                      "| E |Pan con Pollo    |S/7.00 |", "| F |Pan con Jamón    |S/7.00 |",
                      "| G |Pan con Tortilla |S/7.00 |", "| H |=== Lista de pedidos  ===|", leavebar, equalbar]
list3 = len(almuerzo)

cena = [equalbar, "| Cena |", "| A |Pizza Exprés     |S/9.50 |", "| B |Ensalada Campera |S/7.50 |",
                  "| C |Gazpacho         |S/6.00 |", "| D |Caldo de Gallina |S/6.00 |",
                  "| E |Pollo al horno   |S/5.50 |", "| F |Menestrón        |S/4.00 |", leavebar, equalbar]
list4 = len(cena)

############################
#        Selection         #
############################
pricequeue = []
prevqueue = []
while True:
    for list1 in selec1:
        print(list1)
    selection = input("Seleciona una opcion: ")
    if selection == "A":
        for list2 in desayuno:
            print(list2)
        while True:
            orden = input("Seleciona una opcion: ")
            if orden == "A":
                prevqueue.append("Café")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Café", "añadidos a su lista!")
                pricequeue.append(4.50 * float(cantidad))
            elif orden == "B":
                prevqueue.append("Chocolate")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Chocolate", "añadidos a su lista!")
                pricequeue.append(5 * float(cantidad))
            elif orden == "C":
                prevqueue.append("Jugo de Fresas")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Jugo de Fresas", "añadidos a su lista!")
                pricequeue.append(9 * float(cantidad))
            elif orden == "D":
                prevqueue.append("Jugo de Papaya")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Jugo de Papaya", "añadidos a su lista!")
                pricequeue.append(8 * float(cantidad))
            elif orden == "E":
                prevqueue.append("Pan con Pollo")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Pan con Pollo", "añadidos a su lista!")
                pricequeue.append(7 * float(cantidad))
            elif orden == "F":
                prevqueue.append("Pan con Jamón")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Pan con Jamón", "añadidos a su lista!")
                pricequeue.append(7 * float(cantidad))
            elif orden == "G":
                prevqueue.append("Pan con Tortilla")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Pan con Tortilla", "añadidos a su lista!")
                pricequeue.append(7 * float(cantidad))
            elif orden == "H":
                print(equalbar)
                print("Su lista:")
                showqueque = len(prevqueue)
                for showqueque in prevqueue:
                    print(showqueque)
                print(equalbar)
            elif orden == "J":
                break
            else:
                print(equalbar)
                print("|     Seleccion Invalida!     |")
                print(equalbar)
    elif selection == "B":
        for list3 in almuerzo:
            print(list3)
        while True:
            orden1 = input("Seleciona una opcion: ")
            if orden1 == "A":
                prevqueue.append("Café")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Café", "añadidos a su lista!")
                pricequeue.append(4.50 * float(cantidad))
            elif orden1 == "B":
                prevqueue.append("Chocolate")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Chocolate", "añadidos a su lista!")
                pricequeue.append(5 * float(cantidad))
            elif orden1 == "C":
                prevqueue.append("Jugo de Fresas")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Jugo de Fresas", "añadidos a su lista!")
                pricequeue.append(9 * float(cantidad))
            elif orden1 == "D":
                prevqueue.append("Jugo de Papaya")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Jugo de Papaya", "añadidos a su lista!")
                pricequeue.append(8 * float(cantidad))
            elif orden1 == "E":
                prevqueue.append("Pan con Pollo")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Pan con Pollo", "añadidos a su lista!")
                pricequeue.append(7 * float(cantidad))
            elif orden1 == "F":
                prevqueue.append("Pan con Jamón")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Pan con Jamón", "añadidos a su lista!")
                pricequeue.append(7 * float(cantidad))
            elif orden1 == "G":
                prevqueue.append("Pan con Tortilla")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Pan con Tortilla", "añadidos a su lista!")
                pricequeue.append(7 * float(cantidad))
            elif orden1 == "H":
                print(equalbar)
                print("Su lista:")
                showqueque = len(prevqueue)
                for showqueque in prevqueue:
                    print(showqueque)
                print(equalbar)
            elif orden1 == "J":
                break
            else:
                print(equalbar)
                print("|     Seleccion Invalida!     |")
                print(equalbar)
    elif selection == "C":
        for list4 in cena:
            print(list4)
        while True:
            orden2 = input("Seleciona una opcion: ")
            if orden2 == "A":
                prevqueue.append("Pizza Exprés")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Pizza Exprés", "añadidos a su lista!")
                pricequeue.append(9.50 * float(cantidad))
            elif orden2 == "B":
                prevqueue.append("Ensalada Campera")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Ensalada Campera", "añadidos a su lista!")
                pricequeue.append(7.50 * float(cantidad))
            elif orden2 == "C":
                prevqueue.append("Gazpacho")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Gazpacho", "añadidos a su lista!")
                pricequeue.append(6 * float(cantidad))
            elif orden2 == "D":
                prevqueue.append("Caldo de Gallina")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Caldo de Gallina", "añadidos a su lista!")
                pricequeue.append(6 * float(cantidad))
            elif orden2 == "E":
                prevqueue.append("Pollo al horno")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Pollo al horno", "añadidos a su lista!")
                pricequeue.append(7 * float(cantidad))
            elif orden2 == "F":
                prevqueue.append("Menestrón")
                cantidad = solicitar_cantidad()
                print("x", cantidad, "Menestrón", "añadidos a su lista!")
                pricequeue.append(7 * float(cantidad))
            elif orden2 == "H":
                print(equalbar)
                print("Su lista:")
                showqueque = len(prevqueue)
                for showqueque in prevqueue:
                    print(showqueque)
                print(equalbar)
            elif orden2 == "J":
                break
            else:
                print(equalbar)
                print("|     Seleccion Invalida!     |")
                print(equalbar)
    elif selection == "H":
        print(equalbar)
        print("Su lista:")
        showqueque = len(prevqueue)
        for showqueque in prevqueue:
            print(showqueque)
        print(equalbar)
    elif selection == "D":
        print("|      BOLETA DE VENTAS       |")
        print(equalbar)
        subtotal = sum(pricequeue)
        print("| Subtotal:", subtotal)
        IGV = subtotal*0.18
        IGV = round(IGV, 2)
        print("| IGV: " + repr(IGV))
        total = subtotal + IGV
        total = round(total, 2)
        print("| Total a pagar:", total)
        pricequeue.clear()
        prevqueue.clear()
        print("|                             |\n|    Gracias por tu compra!   |")
        print(equalbar)
    else:
        print(equalbar)
        print("|     Seleccion Invalida!     |")
        print(equalbar)
