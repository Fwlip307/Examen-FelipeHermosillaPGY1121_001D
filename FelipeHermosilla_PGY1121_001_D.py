from os import system;system("cls")
import os

evento = [[j + 10 * i for j in range(10)] for i in range(10)]

PLATINUM = 120000
GOLD = 80000
SILVER = 50000

persona = {}

def mostrar_ubicacion():
    print("Estado de las ubicaciones:")
    for fila in evento:
        for ubicacion in fila:
            if ubicacion in persona:
                print("X", end="\t")
            else:
                print(ubicacion, end="\t")
        print()
    print()

def comprar_entrada():
    ubicacion = int(input("Ingrese el número de ubicacion que desea comprar: "))

    if ubicacion in persona:
        print("La ubicacion no está disponible.")
    else:
        rut = int(input("Ingrese el RUN de la persona (sin guiones ni puntos): "))
        persona[ubicacion] = rut
        print("Operacion realizada exitosamente.")

def ubicaciones_disponibles():
    disponibles = 0
    for fila in evento:
        for ubicacion in fila:
            if ubicacion not in persona:
                disponibles += 1
    print(f"Ubicaciones disponibles: {disponibles}")

def lista_ubicaciones():
    if not persona:
        print("No hay personas registradas.")
    else:
        print("Listado de personas:")
        for ubicacion, rut in sorted(persona.items()):
            print(f"Ubicacion {ubicacion}: RUN {rut}")

def ganancias_totales():
    total = 0
    for ubicacion, rut in persona.items():
        if ubicacion <= 20:
            total += PLATINUM
        elif ubicacion <= 50:
            total += GOLD
        else:
            total += SILVER
    print(f"Ganancias totales: ${total}")

while True:
    print("####++++ Menú ++++####")
    print("1. Comprar Entradas")
    print("2. Mostrar Ubicaciones disponibles")
    print("3. Ver Listado de asistentes")
    print("4. Mostrar Ganancias totales")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        mostrar_ubicacion()
        comprar_entrada()
        mostrar_ubicacion()
    elif opcion == "2":
        mostrar_ubicacion()
        ubicaciones_disponibles()
    elif opcion == "3":
        mostrar_ubicacion()
        lista_ubicaciones()
    elif opcion == "4":
        mostrar_ubicacion()
        ganancias_totales()
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")
    
    input("Presione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear") 

print("¡Hasta luego!")
