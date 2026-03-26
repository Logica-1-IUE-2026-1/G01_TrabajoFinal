"""LOGIN"""
#pylint: disable=C0103
acumulador = 0
opcion = 0
if opcion != 2:
    print("♦️  Menu de inicio POKER APAS ♦️")
    print("1. Iniciar sesión")
    print("2. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        while acumulador <= 3:
            if acumulador == 3:
                print("¡USUARIO BLOQUEADO!")
                break
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            if usuario == "esteban" and contrasena == "1234":
                print("Bienvenido, ", usuario)
                break
            else:
                print("Usuario o contraseña incorrectos")
                acumulador += 1
    elif opcion == 2:
        print("Hasta luego...")
    else:
        print("Opción invalida ")
