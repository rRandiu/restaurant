############################
#    Variables Section     #
############################
equalbar = "|=============================|"
leavebar = "| J |========= SALIR =========|"
aj = "A", "B", "C", "D", "E", "F", "G"
ag = "A", "B", "C", "D", "E", "F"

############################
#      Menu Selection      #
############################
selec1 = [equalbar, "|        RESTAURANTE S.A      |", "|            MENÚ             |", equalbar, "| A |Desayuno                 |", "| B |Almuerzo                 |", "| C |Cena                     |", "| D |========= SALIR =========|", equalbar]
list1 = len(selec1)

############################
#          Menus           #
############################
desayuno = [equalbar, "| A |Café             |S/4.50 |", "| B |Chocolate        |S/5.00 |", "| C |Jugo de Fresas   |S/9.00 |", "| D |Jugo de Papaya   |S/8.00 |",
                      "| E |Pan con Pollo    |S/7.00 |", "| F |Pan con Jamón    |S/7.00 |", "| G |Pan con Tortilla |S/7.00 |", leavebar, equalbar]
list2 = len(desayuno)

almuerzo = [equalbar, "| Cena |", "| A |Café             |S/4.50", "| B |Chocolate        |S/5.00", "| C |Jugo de Fresas   |S/9.00", "| D |Jugo de Papaya   |S/8.00",
                      "| E |Pan con Pollo    |S/7.00", "| F |Pan con Jamón    |S/7.00", "| G |Pan con Tortilla |S/7.00", leavebar, equalbar]
list3 = len(almuerzo)

cena = [equalbar, "| Cena |", "| A |Pizza Exprés     |S/9.50 |", "| B |Ensalada Campera |S/7.50 |", "| C |Gazpacho         |S/6.00 |", "| D |Caldo de Gallina |S/6.00 |",
        "| E |Pollo al horno   |S/5.50 |", "| F |Menestrón        |S/4.00 |", leavebar, equalbar]
list4 = len(cena)

############################
#        Selection         #
############################
while True:
 for list1 in selec1:
    print(list1)
 selection = input("Seleciona una opcion: ")
 pricequeue = []
 prevqueue = []
 if selection == "A":
    for list2 in desayuno:
        print(list2)
    while True:
        orden1 = input("Selecione sus platillos: ")
        if orden1 == "A":
            prevqueue.append("Café")
            cantidad = input("Cuantos Café desea?: ")
            pricequeue.append(4.50*float(cantidad))
        elif orden1 == "B":
            prevqueue.append("Chocolate")
            cantidad = input("Cuantos Chocolate desea?: ")
            pricequeue.append(5*float(cantidad))
        elif orden1 == "C":
            prevqueue.append("Jugo de Fresas")
            cantidad = input("Cuantos Jugo de Fresas desea?: ")
            pricequeue.append(9*float(cantidad))
        elif orden1 == "D":
            prevqueue.append("Jugo de Papaya")
            cantidad = input("Cuantos Jugo de Papaya desea?: ")
            pricequeue.append(8*float(cantidad))
        elif orden1 == "E":
            pricequeue.append(7)
            prevqueue.append("Pan con Pollo")
        elif orden1 == "F":
            pricequeue.append(7)
            prevqueue.append("Pan con Jamón")
        elif orden1 == "G":
            pricequeue.append(7)
            prevqueue.append("Pan con Tortilla")
        elif orden1 == "H":
            print("Su lista:")
            showqueque = len(prevqueue)
            for showqueque in prevqueue:
                print(showqueque)
        elif orden1 == "X":
            break
        else:
            print(equalbar)
            print("|     Seleccion Invalida!     |")
            print(equalbar)

 elif selection == "B":
    for list3 in almuerzo:
            print(list3)
    while True:
        orden2 = input("Selecione sus platillos: ")
 elif selection == "C":
    for list4 in cena:
            print(list4)
    while True:
        orden3 = input("Selecione sus platillos: ")

 else:
    print(equalbar)
    print("|     Seleccion Invalida!     |")
    print(equalbar)







