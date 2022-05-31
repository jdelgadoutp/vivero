#Validar nombre de usuario
usuario= input("Ingrese el nombre de usuario: ")
caracteres = len(usuario)
tipo = usuario.isalnum()
if tipo == True:
    if caracteres < 6:
        print("Se debe ingresar como minimo seis(6) caracteres")
    elif caracteres > 8:
        print("Se debe ingresar hasta 8 caracteres")
    else:
        print("Bienvenido a su vivero productor")
else:
    print("El usuario es incorrecto")