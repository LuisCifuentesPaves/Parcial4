import random

compradores = {}

def mostrar_menu():
    print("\nMENU PRINCIPAL")
    print("1. Comprar entrada")
    print("2. Consultar comprador")
    print("3. Cancelar compra")
    print("4. Exit")

def comprar_entrada():
    nombre = input("Ingrese nombre del comprador: ").strip()
    if nombre in compradores:
        print("Este comprador ya tiene una entrada.")
        return
    
    tipo = input("Ingrese tipo de entrada (1, 2, 3 o 4): ").strip()
    if tipo not in ["1", "2", "3", "4"]:
        print("Tipo de entrada inválido.")
        return

    codigo = str(random.randint(100000, 999999))
    compradores[nombre] = {"tipo": tipo, "codigo": codigo}
    print("Compra realizada con éxito.")
    print(f"Código de validación: {codigo}")

def consultar_comprador():
    nombre = input("Ingrese nombre del comprador a buscar: ").strip()
    if nombre in compradores:
        info = compradores[nombre]
        print(f"Tipo de entrada: {info['tipo']}")
        print(f"Código de validación: {info['codigo']}")
    else:
        print("Comprador no encontrado.")

def cancelar_compra():
    nombre = input("Ingrese el nombre del comprador para cancelar la compra: ").strip()
    if nombre in compradores:
        del compradores[nombre]
        print("Compra cancelada exitosamente.")
    else:
        print("Comprador no encontrado.")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        comprar_entrada()
    elif opcion == "2":
        consultar_comprador()
    elif opcion == "3":
        cancelar_compra()
    elif opcion == "4":
        print("Programa terminado.")
        break
    else:
        print("Opción inválida.")


