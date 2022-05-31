#Validar si el codigo ingresado por el usuario es válido

def es_numerico(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

codigo = input('Escriba el codigo: ')

if es_numerico(codigo):
    print('El codigo ingresado es correcto.')
else:
    print('El codigo ingresado no es correcto.')