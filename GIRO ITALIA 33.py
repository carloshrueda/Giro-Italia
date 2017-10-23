def inputContinuarSN(msg):
    opcion = input("\t--> " + msg + " (S/N) ")
    opcion = opcion.upper()
    while opcion != "S" and opcion != "N":
        print("***> Error. Opción inválida. Digite S o N.")
        print("***> Presione cualquier tecla para continuar...")
        input()
        opcion = input("\n\t--> " + msg + " (S/N)")
        opcion = opcion.upper()

    return opcion


def existeEtapa(etapa, etapas):
    # matriz etapas : [[nombre, origen, destino, kilometros]]

    # buscar en la filas la columna 0 de la matriz y si está devolver la posicion de la fila
    # sino devolver -1 por que no está
    for fila in range(len(etapas)):
        if etapas[fila][0] == etapa:
            return fila
    return -1


def existeequipo(equipo, equipos):
    # Busca el equipo en el vector Equipos
    # Si lo encuentra devuelve la posición en donde está
    # Sino, devuelve -1 por que no está
    for i in range(len(equipos)):
        if equipos[i] == equipo:
            return i
    return -1


def existenombreciclista(equipo, nombre, ciclistas):
    # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]

    # recorrer la matrix de ciclistas, fila por fila
    # Si coincide que en la columna 0 (equipo), y columna 2 (nombre)
    # ya existe un ciclista con el mismo nombre, devolver la fila donde está
    # de lo contrario devolver -1
    for fila in range(len(ciclistas)):
        if ciclistas[fila][0] == equipo and ciclistas[fila][2] == nombre:
            return fila
    return -1


def existenumerociclista(numero, ciclistas):
    # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]

    # recorrer la matrix de ciclistas, fila por fila
    # si en la columna 1 de una fila existe el numero devolver el valor la posicion de la fila
    # de lo contrario devolver -1 por que no está
    for fila in range(len(ciclistas)):
        if ciclistas[fila][1] == numero:
            return fila
    return -1


def existeEtapaCiclista(etapa, numero, resuletapas):
    # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]

    for fila in range(len(resuletapas)):
        if etapa == resuletapas[fila][0] and numero == resuletapas[fila][1]:
            return fila
    return -1

def consultarKilometrosCiclistasxEtapas(etapas, ciclistas, resuletapas):
    # matriz etapas : [[nombre, origen, destino, kilometros]]
    # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
    # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]

    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    2. CONSULTAR")
    print("       e. Kilómetros de ciclistas por etapa\n")

    if len(etapas) == 0:
        print("***> Error. No se han ingresado etapas para poder consultar.")
        print("     Presione cualquier tecla para continuar... ")
        input()

    elif len(ciclistas) == 0:
        print("***> Error. No se han ingresado ciclistas para poder consultar.")
        print("     Presione cualquier tecla para continuar... ")
        input()

    elif len(resuletapas) == 0:
        print("***> Error. No se han ingresado resultados por etapa para poder consultar.")
        print("     Presione cualquier tecla para continuar... ")
        input()

    else:
        opcion = ""
        while opcion != "N":
            etapa = input("\nNombre de la etapa que desea consultar? ")
            etapa = etapa.strip()
            if len(etapa) == 0:
                # nombre equipo invalido. vacio
                print("***> Error, Nombre de la etapa inválido. Intente nuevamente.")

            else:
                # si no es vacío hacer
                etapa = etapa.upper()
                fila = existeEtapa(etapa, etapas)
                if fila == -1:
                    # no existe la etapa
                    print("---> La etapa no existe")
                else:
                    # la etapa existe
                    # preguntar por el número del ciclista y validar si este existe
                    numero = input("Número del Ciclista? ")
                    numero = numero.strip()
                    if len(numero) == 0:
                        # numero vacío
                        print("***> Error, número de ciclista inválido. Intente nuevamente")
                    else:
                        # numero valido, entonces validar si el ciclista existe
                        filanuci = existenumerociclista(numero, ciclistas)
                        if filanuci == -1:
                            # No existe el número del ciclistas
                            print("***> Error, el ciclista con ese número no ha sido registrado. Intente nuevamente")
                        else:
                            # Si existe el número del ciclista,
                            # entonces buscar el resultado del ciclista en la etapa
                            filEtaCi = existeEtapaCiclista(etapa, numero, resuletapas)
                            if filEtaCi == -1:
                                # No existe datos del ciclista en la etapa
                                print("***> Error, no hay datos del ciclista en la etapa")
                            else:
                                # existen datos para el ciclista en la etapa
                                # Imprimir datos
                                origen = etapas[fila][1]
                                destino = etapas[fila][2]
                                kmetapa = etapas[fila][3]
                                nomequipo = ciclistas[filanuci][0]
                                nomciclista = ciclistas[filanuci][2]
                                kmEtapaCi = resuletapas[filEtaCi][3]

                                print("")
                                print("Etapa: ", etapa)
                                print("Origen de la etapa: ", origen)
                                print("Destino de la etapa: ", destino)
                                print("Kilometros de la etapa", kmetapa)
                                print("")
                                print("Numero del ciclista: ", numero)
                                print("Nombre del ciclista: ", nomciclista)
                                print("Equipo del ciclista: ", nomequipo)
                                print("* Kilometros del cilista en la etapa", kmEtapaCi)

            print("")
            opcion = inputContinuarSN("Desea consultar otra etapa?")
            print("")

def consultarKilometrosxEtapas(etapas):
    # matriz etapas : [[nombre, origen, destino, kilometros]]

    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    2. CONSULTAR")
    print("       d. Kilómetros de cada etapa\n")

    if len(etapas) == 0:
        print("***> Error. No se han ingresado etapas para poder consultar.")
        print("     Presione cualquier tecla para continuar... ")
        input()

    else:
        opcion = ""
        while opcion != "N":
            etapa = input("\nNombre de la etapa que desea consultar? ")
            etapa = etapa.strip()
            if len(etapa) == 0:
                # nombre equipo invalido. vacio
                print("***> Error, Nombre de la etapa inválido. Intente nuevamente.")

            else:
                # si no es vacío hacer
                etapa = etapa.upper()
                fila = existeEtapa(etapa, etapas)
                if fila == -1:
                    # no existe la etapa
                    print("---> La etapa no existe")
                else:
                    #la etapa existe
                    kmetapa= etapas[fila][3]
                    if kmetapa <= 0:
                        # los kilometros no han sido ingresaados
                        print("---> Los kilometros no han sido ingresados.")
                    else:
                        print("Nombre de la etapa: ", etapa)
                        print("Kilometros: ", etapas[fila][3])

            print("")
            opcion = inputContinuarSN("Desea consultar otra etapa?")
            print("")


def consultarEtapas(etapas):
    # matriz etapas : [[nombre, origen, destino, kilometros]]


    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    2. CONSULTAR")
    print("       c. Etapas\n")

    if len(etapas) == 0:
        print("***> Error. No se han ingresado etapas para poder consultar.")
        print("     Presione cualquier tecla para continuar... ")
        input()

    else:
        opcion = ""
        while opcion != "N":
            etapa = input("\nNombre de la etapa que desea consultar? ")
            etapa = etapa.strip()
            if len(etapa) == 0:
                # nombre equipo invalido. vacio
                print("***> Error, Nombre de la etapa inválido. Intente nuevamente.")

            else:
                # si no es vacío hacer
                etapa = etapa.upper()
                fila = existeEtapa(etapa, etapas)
                if fila == -1:
                    # no existe la etapa
                    print("---> La etapa no existe")
                else:
                    print("---> La etapa existe.\n")

                    print("Nombre de la etapa: ", etapa)
                    print("Lugar de origen: ", etapas[fila][1])
                    print("Lugar de destino: ", etapas[fila][2])

            print("")
            opcion = inputContinuarSN("Desea consultar otra etapa?")
            print("")


def consultarCiclistaxEquipos(equipos, ciclistas):
    # vector equipos [nombreequipo]
    # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]

    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    2. CONSULTAR")
    print("       b. Ciclistas por equipos\n")

    if len(equipos) == 0:
        print("***> Error. No se han ingresado equipos para poder consultar.")
        print("     Presione cualquier tecla para continuar... ")
        input()

    else:
        opcion = ""
        while opcion != "N":
            equipo = input("Nombre del equipo que desea consultar? ")
            equipo = equipo.strip()
            if len(equipo) == 0:
                # si el nombre del equipo es vacío
                print("***> Error. Nombre inválido para un equipo.")

            else:
                # si el nombre del equipo no es vacio
                equipo = equipo.upper()
                filaeq = existeequipo(equipo, equipos)
                if filaeq == -1:
                    # Si no existe el equipo
                    print("***> Este equipo no existe. Intente nuevamente.")

                else:
                    # si existe el equipo
                    print("---------------------")
                    print("\n EQUIPO: " + equipo)
                    print("---------------------")
                    print("\nNUMERO\tCICLISTAS: ")
                    # recorrer la matriz ciclistas y sacar los ciclistas de dicho equipo
                    contadorcilistas = 0
                    for fila in range(len(ciclistas)):
                        if ciclistas[fila][0] == equipo:
                            # si una fila
                            contadorcilistas = contadorcilistas + 1
                            print(ciclistas[fila][1] + "\t" + "     " + ciclistas[fila][2])

                    if contadorcilistas == 0:
                        # si despues de recorrer la matriz ciclistas no se encuentra ciclistas en ese equipo
                        print("---> No hay ciclistas agregados a dicho equipo.")

            print("")
            opcion = inputContinuarSN("Desea continuar agregando ciclistas al equipo?")
            print("")


def consultarEquipos(equipos):
    # vector equipos [nombreequipo]

    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    1. CONSULTAR")
    print("       a. Equipos de Ciclismo\n")

    if len(equipos) == 0:
        print("***> Error. No se han ingresado equipos para poder consultar.")
        print("     Presione cualquier tecla para continuar... ")
        input()

    else:
        opcion = ""
        while opcion != "N":
            nombequipo = input("\nNombre del equipo que desea consultar? ")
            nombequipo = nombequipo.strip()
            if len(nombequipo) > 0:
                # si no es vacío hacer
                # si el equipo no existe agregar, sino, enviar un mensaje y no agregar
                nombequipo = nombequipo.upper()
                fila = existeequipo(nombequipo, equipos)
                if fila == -1:
                    # no existe el equipo
                    print("---> El equipo no existe")
                else:
                    print("---> El equipo existe.")

            else:
                # nombre equipo invalido
                print("***> Error, Nombre de equipo inválido. Intente nuevamente.")

            print("")
            opcion = inputContinuarSN("Desea consultar otro equipo de ciclismo?")
            print("")


def printmenuConsultar():
    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    4. CONSULTAR")
    print("a. Equipos de Ciclismo")
    print("b. Ciclistas por equipos")
    print("c. Etapas")
    print("d. Kilómetros de cada etapa")
    print("e. Kilómetros de ciclistas por etapa")
    print("f. Tiempo del ciclista por etapa")
    print("g. Salir\n")


def menuConsultar(equipos, ciclistas, etapas, resuletapas):
    opcion = ""
    while opcion != "G":
        printmenuConsultar()
        opcion = input("   Opcion (a-g)? ")
        opcion = opcion.upper()

        # si el usuario digita algo diferente a-g
        # hacer hasta que el usuario digite una opcion válida
        while opcion < "A" or opcion > "G":
            print("***> Error. Opción inválida del menu. Escoja (a-g)")
            print("***> Presiones cualqueir tecla para continuar ...")
            input()
            printmenuRegistrar()
            opcion = input("   Opción (a-g)? ")
            opcion = opcion.upper()

        # Despues de que el usuario haya digitado una buena opcion
        if opcion == "A":
            # vector equipos [nombreequipo]
            consultarEquipos(equipos)

        elif opcion == "B":
            # vector equipos [nombreequipo]
            # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
            consultarCiclistaxEquipos(equipos, ciclistas)

        elif opcion == "C":
            # matriz etapas : [[nombre, origen, destino, kilometros]]
            consultarEtapas(etapas)

        elif opcion == "D":
            # matriz etapas : [[nombre, origen, destino, kilometros]]
            consultarKilometrosxEtapas(etapas)

        elif opcion == "E":
            # matriz etapas : [[nombre, origen, destino, kilometros]]
            # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
            # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]
             consultarKilometrosCiclistasxEtapas(etapas, ciclistas, resuletapas)

        elif opcion == "F":
            # matriz etapas : [[nombre, origen, destino, kilometros]]
            # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
            # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]
            # consultarTiempoCiclistaxEtapa(etapas, ciclistas, resuletapas)
            pass


def ingresarTiempoCiclistaxEtapa(etapas, ciclistas, resuletapas):
    # matriz etapas : [[nombre, origen, destino, kilometros]]
    # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
    # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]

    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    1. REGISTAR")
    print("       f. Tiempo del ciclista por etapa\n")

    opcion = ""
    while opcion != "N":
        etapa = input("\nNombre de la Etapa? ")
        etapa = etapa.strip()
        if len(etapa) == 0:
            # Etapa vacia
            print("***> Error, nombre de etapa inválido. Intente nuevamente")
        else:
            # Nombre de la etapa no es vacio
            etapa = etapa.upper()
            filaet = existeEtapa(etapa, etapas)
            if filaet == -1:
                # No existe la etapa
                print("***> Error, la etapa no ha sido registrada. Intente nuevamente")
            else:
                # Existe la etapa
                numero = input("Número del Ciclista? ")
                numero = numero.strip()
                if len(numero) == 0:
                    # numero vacío
                    print("***> Error, número de ciclista inválido. Intente nuevamente")
                else:
                    # numero valido
                    filanuci = existenumerociclista(numero, ciclistas)
                    if filanuci == -1:
                        # No existe el número del ciclistas
                        print("***> Error, el ciclista con ese número no ha sido registrado. Intente nuevamente")
                    else:
                        # Si existe el número del ciclista

                        tiempo = input("Tiempo del ciclista? ")
                        tiempo = tiempo.strip()
                        if len(tiempo) == 0:
                            # kilometros vacios
                            print("***> Error, Valor del tiempo inválido. Intente nuevamente")
                        else:
                            ti = float(tiempo)
                            if ti < 1:
                                # kilometros cero o negativos
                                print("***> Error, Valor del tiempo inválido. Intente nuevamente")
                            else:
                                # kilometros validos
                                # agrega o modifica los kilometros al ciclista 
                                # en la etapa

                                filEtaCi = existeEtapaCiclista(etapa, numero, resuletapas)
                                if filEtaCi == -1:
                                    # No existe datos en la etapa de dicho ciclista
                                    # agrega
                                    resuletapas.append([etapa, numero, 0, ti])
                                else:
                                    # existen datos para el ciclista en la etapa
                                    # modificar
                                    tiempoant = resuletapas[filEtaCi][3]
                                    if tiempoant == 0:
                                        # si es cero, modifica sin problema
                                        resuletapas[filEtaCi][3] = ti
                                    else:
                                        # ya se habia registrado un tiempo
                                        modificar = inputContinuarSN("Existe un tiempo registrado. Desea modificarlo?")
                                        if modificar == "S":
                                            resuletapas[filEtaCi][3] = ti

        opcion = inputContinuarSN("Desea continuar?")


def ingresarKilometrosCiclistasxEtapas(etapas, ciclistas, resuletapas):
    # matriz etapas : [[nombre, origen, destino, kilometros]]
    # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
    # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]

    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    1. REGISTAR")
    print("       e. Kilómetros de ciclistas por etapa\n")

    opcion = ""
    while opcion != "N":
        etapa = input("\nNombre de la Etapa? ")
        etapa = etapa.strip()
        if len(etapa) == 0:
            # Etapa vacia
            print("***> Error, nombre de etapa inválido. Intente nuevamente")
        else:
            # Nombre de la etapa no es vacio
            etapa = etapa.upper()
            filaet = existeEtapa(etapa, etapas)
            if filaet == -1:
                # No existe la etapa
                print("***> Error, la etapa no ha sido registrada. Intente nuevamente")
            else:
                # Existe la etapa
                numero = input("Número del Ciclista? ")
                numero = numero.strip()
                if len(numero) == 0:
                    # numero vacío
                    print("***> Error, número de ciclista inválido. Intente nuevamente")
                else:
                    # numero valido
                    filanuci = existenumerociclista(numero, ciclistas)
                    if filanuci == -1:
                        # No existe el número del ciclistas
                        print("***> Error, el ciclista con ese número no ha sido registrado. Intente nuevamente")
                    else:
                        # Si existe el número del ciclista
                        kilometros = input("Kilometros recorridos por el ciclista? ")
                        kilometros = kilometros.strip()
                        if len(kilometros) == 0:
                            # kilometros vacios
                            print("***> Error, kilometros inválidos. Intente nuevamente")
                        else:
                            km = float(kilometros)
                            if km < 1:
                                # kilometros cero o negativos
                                print("***> Error, kilometros inválidos. Intente nuevamente")
                            else:
                                # kilometros validos
                                # agrega los kilometros al ciclista en la etapa
                                kmetapa = etapas[filaet][3]
                                if km > kmetapa:
                                    print("***> Error, el ciclista no puede recorrer más Km que la etapa")
                                    print("     Km de la etapa: ", kmetapa)
                                    print("     Km que intenta ingresar: ", km)
                                else:
                                    resuletapas.append([etapa, numero, km, 0])

        opcion = inputContinuarSN("Desea continuar?")


def ingresarKilometrosxEtapas(etapas):
    # matriz etapas : [[nombre, origen, destino, kilometros]]


    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    1. REGISTAR")
    print("       d. Kilómetros de cada etapa\n")

    opcion = ""
    while opcion != "N":
        etapa = input("\nNombre de la Etapa a la que desea ingresar los kilómetros? ")
        etapa = etapa.strip()
        if len(etapa) > 0:
            # si el nombre de la estapa no está vacío
            etapa = etapa.upper()
            fila = existeEtapa(etapa, etapas)
            if fila == -1:
                # Si ya existe una estapa con ese nombre
                print("***> Error, esa etapa no ha sido registrada. Intente nuevamente")
            else:
                # si existe la etapa
                kilometros = float(input("Ingrese los kilometros de la estapa? "))
                if kilometros > 0:
                    # si los kilometros son positivos
                    # modificar el valor de kilómetro que está en
                    # la columna 3
                    etapas[fila][3] = kilometros
                else:
                    # kilometros es un numero negativo y por lo tanto inválido
                    print("***> Error, valor inválido para los kilómetros. Intente nuevamente")
        else:
            print("***> Error, nombre de etapa inválido. Intente nuevamente")

        opcion = inputContinuarSN("Desea continuar?")


def ingresarEtapas(etapas):
    # matriz etapas : [[nombre, origen, destino, kilometros]]

    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    1. REGISTAR")
    print("       c. Etapas\n")

    opcion = ""
    while opcion != "N":
        etapa = input("\nNombre de la Etapa que desea ingresar? ")
        etapa = etapa.strip()
        if len(etapa) > 0:
            etapa = etapa.upper()
            fila = existeEtapa(etapa, etapas)
            if fila > -1:
                # Si no existe una estapa con ese nombre
                print("***> Error, una etapa con ese nombre ya fue registrada. Intente nuevamente")
            else:
                # si no existe una etapa con ese nombre
                origen = input("Lugar de inicio de la etapa? ")
                origen.strip()
                if len(origen) > 0:
                    # Si el origen no es vacio
                    destino = input("Lugar de finalización de la etapa? ")
                    destino = destino.strip()
                    if len(destino) > 0:
                        # Si el destino no es vacio entonces agregar la etapa
                        # se agrega kilometros 0 por que aun no tiene un dato válidlo
                        etapas.append([etapa, origen, destino, 0])
                    else:
                        # si el destino es vacio
                        print("***> Error, lugar de destino inválido. Intente nuevamente")
                else:
                    # si el origen es vacio
                    print("***> Error, lugar de origen inválido. Intente nuevamente")
        else:
            print("***> Error, nombre de etapa inválido. Intente nuevamente")

        opcion = inputContinuarSN("Desea continuar agregando etapas?")


def ingresarCiclistaxEquipos(equipos, ciclistas):
    # vector equipos [nombreequipo]
    # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]


    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    1. REGISTAR")
    print("       b. Ciclistas por equipos\n")

    if len(equipos) == 0:
        print("***> Error. No se han ingresado equipos")
        print("     Presione cualquier tecla para continuar... ")
        input()
        return
    else:

        equipo = input("Nombre del Equipo a quien desea ingresar ciclistas? ")
        equipo = equipo.strip()
        if len(equipo) > 0:
            # si no es vacío
            equipo = equipo.upper()
            filaeq = existeequipo(equipo, equipos)
            if filaeq == -1:
                # Si no existe el equipo
                print("***> Error, este equipo no ha sido ingresado. Intente nuevamente.")
                print("     Presione cualquier tecla para continuar")
                input()
            else:
                opcion = ""
                while opcion != "N":
                    # si existe el equipo
                    numero = input("\nNúmero del ciclista? ")
                    numero = numero.strip()
                    if len(numero) > 0:
                        # si no está vacío
                        filanuci = existenumerociclista(numero, ciclistas)
                        if filanuci == -1:
                            # si no existe el número del ciclista
                            nombre = input("Nombre del ciclista? ")
                            nombre = nombre.strip()
                            if len(nombre) > 0:
                                # si el nombre no está vacio
                                nombre = nombre.upper()
                                filanoci = existenombreciclista(equipo, nombre, ciclistas)
                                if filanoci == -1:
                                    # no está el nombre del ciclista
                                    # agregar al equipo, el ciclista con su numero
                                    ciclistas.append([equipo, numero, nombre])
                                else:
                                    print(
                                        "***> Error, Un ciclista con ese nombre ya existe en el equipo. Intente nuevamente")
                            else:
                                print("***> Error, nombre inválido para un ciclista. Intente nuevamente")
                        else:
                            print("***> Error, ese número ya existe para otro ciclista. Intente nuevamente")
                    else:
                        print("***> Error, número inválido para un ciclista. Intente nuevamente")

                    opcion = inputContinuarSN("Desea continuar agregando ciclistas al equipo?")
        else:
            print("***> Error. Nombre inválido para un equipo.")


def ingresarEquipos(equipos):
    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    1. REGISTAR")
    print("       a. Equipos de Ciclismo\n")
    opcion = ""
    while opcion != "N":
        nombequipo = input("\nNombre del equipo? ")
        nombequipo = nombequipo.strip()
        if len(nombequipo) > 0:
            # si no es vacío hacer
            # si el equipo no existe agregar, sino, enviar un mensaje y no agregar
            nombequipo = nombequipo.upper()
            fila = existeequipo(nombequipo, equipos)
            if fila == -1:
                # no existe el equipo
                equipos.append(nombequipo)
            else:
                print("***> Error. El equipo ya existe.")

        opcion = inputContinuarSN("Desea agregar otro equipo de ciclismo?")


def printmenuRegistrar():
    # limpia la consola

    # dibuja el menu
    print("--- MENU GIRO ITALIA---\n")
    print("    1. REGISTAR")
    print("a. Equipos de Ciclismo")
    print("b. Ciclistas por equipos")
    print("c. Etapas")
    print("d. Kilómetros de cada etapa")
    print("e. Kilómetros de ciclistas por etapa")
    print("f. Tiempo del ciclista por etapa")
    print("g. Salir\n")


def menuRegistrar(equipos, ciclistas, etapas, resuletapas):
    opcion = ""
    while opcion != "G":
        printmenuRegistrar()
        opcion = input("   Opcion (a-g)? ")
        opcion = opcion.upper()

        # si el usuario digita algo diferente a-g
        # hacer hasta que el usuario digite una opcion válida
        while opcion < "A" or opcion > "G":
            print("***> Error. Opción inválida del menu. Escoja (a-g)")
            print("***> Presiones cualqueir tecla para continuar ...")
            input()
            printmenuRegistrar()
            opcion = input("   Opción (a-g)? ")
            opcion = opcion.upper()

        # Despues de que el usuario haya digitado una buena opcion
        if opcion == "A":
            # vector equipos [nombreequipo]
            ingresarEquipos(equipos)

        elif opcion == "B":
            # vector equipos [nombreequipo]
            # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
            ingresarCiclistaxEquipos(equipos, ciclistas)

        elif opcion == "C":
            # matriz etapas : [[nombre, origen, destino, kilometros]]
            ingresarEtapas(etapas)

        elif opcion == "D":
            # matriz etapas : [[nombre, origen, destino, kilometros]]
            ingresarKilometrosxEtapas(etapas)

        elif opcion == "E":
            # matriz etapas : [[nombre, origen, destino, kilometros]]
            # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
            # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]
            ingresarKilometrosCiclistasxEtapas(etapas, ciclistas, resuletapas)

        elif opcion == "F":
            # matriz etapas : [[nombre, origen, destino, kilometros]]
            # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
            # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]
            ingresarTiempoCiclistaxEtapa(etapas, ciclistas, resuletapas)


def menuEditar(equipos, ciclistas, etapas, resuletapas):
    pass


def menu():
    # Función que dibuja en la pantalla las opciones del menu

    # imprimir el menu en la pantalla
    print("--- MENU GIRO ITALIA---\n")
    print("1. REGISTRAR")
    print("2. CONSULTAR")
    print("3. SALIR\n")


def inicio():
    opcion = ""
    # vector equipos [nombreequipo]
    equipos = []  # lista de los equipos. Vacío
    # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
    ciclistas = []
    # matriz etapas : [[nombre, origen, destino, kilometros]]
    etapas = []  # lista de las etapas. Vacío
    # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]
    resuletapas = []  # Resultadas por estapas. Vacío

    opcion = ""
    # mientras la opción sea diferente a salir (opcion 5)
    while (opcion != "3"):
        # dibujar el menu en la pantalla
        menu()
        opcion = input("   Opcion (1-3)? ")
        # si el usuario digita una opción invalida entonces
        # haga un ciclo hasta que digite una opcion válida
        while opcion < "1" or opcion > "3":
            print("***> Error. Opción inválida del menu. Escoja (1-3)")
            print("***> Presiones cualqueir tecla para continuar ...")
            input()
            menu()
            opcion = input("   Opción (1-3)? ")

        if opcion == "1":
            menuRegistrar(equipos, ciclistas, etapas, resuletapas)
        elif opcion == "2":
            menuConsultar(equipos, ciclistas, etapas, resuletapas)
        elif opcion == "3":
            print("Gracias por usar el software")
            print("--- ADIOS ---")


#### PROGRAMA PRINCIPAL ####
if __name__ == "__main__":
    inicio()
