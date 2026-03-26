"""MENU"""
#pylint: disable=C0103

print("♦️ Menu de interaccion de POKER APAS ♦️")
opcion = int(input(" 1. Menu general \n 2. Menu jugadores \n 3. Menu Administrador \n"))

if opcion == 1:
    print("♦️ Menu general de POKER APAS ♦️")
    opcion2 = int(input("1. Ver resultados \n 2. Salir \n"))
    if opcion2 == 1:
        print(
            "Resultados: \n ♠️  Ganaste una partida el 12/03/2026 a las 3:00pm \n \
            ♠️  Perdiste una partida el 12/03/2026 a las 3:00pm \n"
            )
    else:
        print("Hasta pronto...")
elif opcion == 2:
    print("♦️ Menu de juego POKER APAS ♦️")
    opcion2 = int(input("1. Nueva partida \n 2. Salir \n"))
    if opcion2 == 1:
        print("jugando... partida en curso")
    else:
        print("Hasta luego...")
elif opcion == 3:
    print("♦️ Menu de administrador POKER APAS ♦️")
    opcion2 = int(input(
        "1. Consultar resultados \n 2. Bloquear usuario \n 3. Desbloquear usuario \n 4. Salir \n"
        ))
    if opcion2 == 1:
        print(
            "Resultados: \n ♠️  Jair Gano una partida el 12/03/2026 a las 3:00pm \n \
            ♠️  Jonatan Perdio una partida el 12/03/2026 a las 3:00pm \n"
            )
    elif opcion2 == 2:
        usubloq = input("Que usuario desea bloquear: \n ")
        print(f"Usario {usubloq} bloqueado con exito")
    elif opcion2 == 3:
        usubloq = input("Que usuario desea desbloquear: \n ")
        print(f"Usario {usubloq} desbloqueado con exito")
    else:
        print("Hasta luego...")
