import os

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
    #Busca el equipo en el vector Equipos
    #Si lo encuentra devuelve la posición en donde está
    #Sino, devuelve -1 por que no está
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
            #Etapa vacia
            print("***> Error, nombre de etapa inválido. Intente nuevamente")
        else:
            #Nombre de la etapa no es vacio
            etapa= etapa.upper()
            filaet= existeEtapa(etapa, etapas)
            if filaet == -1:
                #No existe la etapa
                print("***> Error, la etapa no ha sido registrada. Intente nuevamente")
            else:
                # Existe la etapa
                numero = input("Número del Ciclista? ")
                numero = numero.strip()
                if len(numero) == 0:
                    #numero vacío
                    print("***> Error, número de ciclista inválido. Intente nuevamente")
                else:
                    #numero valido
                    filanuci= existenumerociclista(numero, ciclistas)
                    if filanuci == -1:
                        #No existe el número del ciclistas
                        print("***> Error, el ciclista con ese número no ha sido registrado. Intente nuevamente")
                    else:
                        #Si existe el número del ciclista
                        
                        tiempo= input("Tiempo del ciclista? ")
                        tiempo = tiempo.strip()
                        if len(tiempo) == 0:
                            #kilometros vacios
                            print("***> Error, Valor del tiempo inválido. Intente nuevamente")
                        else:
                            ti= float(tiempo)
                            if ti < 1:
                                # kilometros cero o negativos
                                print("***> Error, Valor del tiempo inválido. Intente nuevamente")
                            else:
                                # kilometros validos
                                # agrega o modifica los kilometros al ciclista 
                                # en la etapa
                                
                                filEtaCi= existeEtapaCiclista(etapa, numero, resuletapas)
                                if filEtaCi == -1:
                                    #No existe datos en la etapa de dicho ciclista
                                    #agrega
                                    resuletapas.append([etapa, numero, 0, ti])
                                else:
                                    #existen datos para el ciclista en la etapa
                                    #modificar
                                    tiempoant= resuletapas[filEtaCi][3]
                                    if tiempoant == 0:
                                        #si es cero, modifica sin problema
                                        resuletapas[filEtaCi][3]= ti
                                    else:
                                        #ya se habia registrado un tiempo
                                        modificar= inputContinuarSN("Existe un tiempo registrado. Desea modificarlo?")
                                        if modifica == "S":
                                            resuletapas[filEtaCi][3]= ti
                            
                                
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
            #Etapa vacia
            print("***> Error, nombre de etapa inválido. Intente nuevamente")
        else:
            #Nombre de la etapa no es vacio
            etapa= etapa.upper()
            filaet= existeEtapa(etapa, etapas)
            if filaet == -1:
                #No existe la etapa
                print("***> Error, la etapa no ha sido registrada. Intente nuevamente")
            else:
                # Existe la etapa
                numero = input("Número del Ciclista? ")
                numero = numero.strip()
                if len(numero) == 0:
                    #numero vacío
                    print("***> Error, número de ciclista inválido. Intente nuevamente")
                else:
                    #numero valido
                    filanuci= existenumerociclista(numero, ciclistas)
                    if filanuci == -1:
                        #No existe el número del ciclistas
                        print("***> Error, el ciclista con ese número no ha sido registrado. Intente nuevamente")
                    else:
                        #Si existe el número del ciclista
                        kilometros= input("Kilometros recorridos por el ciclista? ")
                        kilometros = kilometros.strip()
                        if len(kilometros) == 0:
                            #kilometros vacios
                            print("***> Error, kilometros inválidos. Intente nuevamente")
                        else:
                            km= float(kilometros)
                            if km < 1:
                                # kilometros cero o negativos
                                print("***> Error, kilometros inválidos. Intente nuevamente")
                            else:
                                # kilometros validos
                                # agrega los kilometros al ciclista en la etapa
                                kmetapa= etapas[filaet][3]
                                if km > kmetapa:
                                    print("***> Error, el ciclista no puede recorrer más Km que la etapa")
                                    print("     Km de la etpa: ", km)
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
            #si el nombre de la estapa no está vacío
            etapa = etapa.upper()
            fila= existeEtapa(etapa, etapas)
            if fila == -1:
                # Si ya existe una estapa con ese nombre
                print("***> Error, esa etapa no ha sido registrada. Intente nuevamente")
            else:
                #si existe la etapa
                kilometros= float(input("Ingrese los kilometros de la estapa? "))
                if kilometros>0:
                    #si los kilometros son positivos
                    #modificar el valor de kilómetro que está en
                    # la columna 3
                    etapas[fila][3] = kilometros
                else:
                    #kilometros es un numero negativo y por lo tanto inválido
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
                #Si no existe una estapa con ese nombre
                print("***> Error, una etapa con ese nombre ya fue registrada. Intente nuevamente")
            else:
                #si no existe una etapa con ese nombre
                origen= input("Lugar de inicio de la etapa? ")
                origen.strip()
                if len(origen)>0:
                    #Si el origen no es vacio
                    destino= input("Lugar de finalización de la etapa? ")
                    destino = destino.strip()
                    if len(destino)>0:
                        #Si el destino no es vacio entonces agregar la etapa
                        # se agrega kilometros 0 por que aun no tiene un dato válidlo
                        etapas.append([etapa, origen, destino, 0])
                    else:
                        #si el destino es vacio
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
            filaeq= existeequipo(equipo, equipos)
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
                        filanuci= existenumerociclista(numero, ciclistas)
                        if filanuci == -1:
                            # si no existe el número del ciclista
                            nombre = input("Nombre del ciclista? ")
                            nombre = nombre.strip()
                            if len(nombre) > 0:
                                # si el nombre no está vacio
                                nombre = nombre.upper()
                                filanoci= existenombreciclista(equipo, nombre, ciclistas)
                                if filanoci == -1:
                                    #no está el nombre del ciclista
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
    # vector equipos [nombreequipo]

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
            fila= existeequipo(nombequipo, equipos)
            if fila == -1:
                #no existe el equipo
                equipos.append(nombequipo)
            else:
                print("***> Error. El equipo ya existe.")

        opcion = inputContinuarSN("Desea agregar otro equipo de ciclismo?")


def printmenuRegistrar():
    # limpia la consola
    os.system("CLS")

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
    nomArch = "GiroItalia.txt"
    opcion = ""
    # vector equipos [nombreequipo]
    equipos = []  # lista de los equipos. Vacío
     # matrix ciclistas [ [nomequipo, numero, nombreciclista] ]
    ciclistas = []
    # matriz etapas : [[nombre, origen, destino, kilometros]]
    etapas = []  # lista de las etapas. Vacío
    # matriz resuletapas : [[nombreEtapa, numCiclista, kilometros, tiempo]]
    resuletapas = []  # Resultadas por estapas. Vacío


    # preguntar si el archivo ya existe o no
    # si existe cargar los datos a las variables
    # si no existe crearlo vaciio
    if os.path.exists(nomArch):
        # si existe el archivo
        # preguntar al usuario si quiere que el archivo se carge
        # o se cree uno nuevo
        print("Ya existe un archivo con un Giro registrado.")
        opcion = input("---> Desea cargarlo o crear uno nuevo?  (S: cargarlo / N: crearlo) ")
        opcion = opcion.upper()  # coloca en mayusculas la opción digitada por el usuario
        # si el usuario digita algo diferente al S o N entonces hacer un ciclo hasta que digite bien
        while opcion != "S" and opcion != "N":
            print("***> Error. Opción inválida. Digite S o N.\n")
            print("Ya existe un archivo con un Giro registrado.")
            opcion = input("--> Desea cargarlo o crear uno nuevo?  (S: cargarlo / N: crearlo) ")
            opcion = opcion.upper()

        if opcion == "S":
            # Abrir el archivo en modo lectura
            archivo = open(nomArch, "r")
            # Cargar el archivo a las variables
            archivo.close()
        else:
            # Abrir el archivo en modo escritura esto hace que se cree el archivo vacío
            archivo = open(nomArch, "w")
            archivo.close()

    else:
        # si no existe el archivo
        # Abrir el archivo en modo escritura esto hace que se cree el archivo vacío
        archivo = open(nomArch, "w")
        archivo.close()

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
