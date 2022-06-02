#Validación de Departamento-Ciudad

ciudades = {}


def agregar_departamento_ciudad(departamento, ciudad):
    global ciudades
    if not ciudad in ciudades:
        ciudades[ciudad] = []
    ciudades[ciudad].append(departamento)


def imprimir_departamentos_de_ciudad(ciudad):
    if not ciudad in ciudades:
        print("No hay departamento registrados")
        return

    print("Los departamento de " + ciudad + " son: ")
    for departamento in ciudades[ciudad]:
        print(departamento)


eleccion = ""
while eleccion != "3":
    eleccion = input("""
1. Agregar departamento
2. Mostrar departamento de ciudad
3. Salir
Seleccione: """)
    if eleccion == "1":
        departamento = input("Ingrese el departamento: ")
        ciudad = input("Ingrese la ciudad al que pertenece: ")
        agregar_departamento_ciudad(departamento, ciudad)
        print("Agregado")
    elif eleccion == "2":
        ciudad = input("Ingrese la ciudad: ")
        imprimir_departamentos_de_ciudad(ciudad)