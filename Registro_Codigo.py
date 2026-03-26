"""REGISTRO"""
#pylint: disable=C0103

Opcion = 0

#Registro de usuario
if Opcion != 2:
    print("♦️  Menu de registro POKER APAS ♦️")
    print("1. Registrar usuario")
    print("2. Salir")
    opcion = int(input("Seleccione una opción: "))
if Opcion == 1:
    nuevo_usuario = input("Registre su usuario: ")
    nueva_contrasena = input("Ingrese una nueva contraseña: ")
    print("Usuario registrado")
else:
    print("Hasta Luego...")
