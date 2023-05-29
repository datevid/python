def particionar_jugadores(jugadores, grupos, grupo_actual, suma_objetivo):
    if grupo_actual == len(jugadores):
        if all(sum(jugador['peso'] for jugador in grupo) == suma_objetivo for grupo in grupos):
            return grupos
        else:
            return None

    jugador = jugadores[grupo_actual]

    # Probar agregar el jugador al grupo existente
    for grupo in grupos:
        grupo.append(jugador)
        solucion = particionar_jugadores(jugadores, grupos, grupo_actual + 1, suma_objetivo)
        if solucion:
            return solucion
        grupo.pop()

    # Probar crear un nuevo grupo con el jugador
    if len(grupos) < 3:
        grupos.append([jugador])
        solucion = particionar_jugadores(jugadores, grupos, grupo_actual + 1, suma_objetivo)
        if solucion:
            return solucion
        grupos.pop()

    return None

jugadores = [
    {'nombre': 'Jugador1', 'peso': 5},
    {'nombre': 'Jugador2', 'peso': 2},
    {'nombre': 'Jugador3', 'peso': 3},
    {'nombre': 'Jugador4', 'peso': 2},
    {'nombre': 'Jugador5', 'peso': 4},
    {'nombre': 'Jugador6', 'peso': 4},
    {'nombre': 'Jugador11', 'peso': 4},
    {'nombre': 'Jugador12', 'peso': 5},
    {'nombre': 'Jugador13', 'peso': 6},
    {'nombre': 'Jugador14', 'peso': 2},
    {'nombre': 'Jugador15', 'peso': 2},
    {'nombre': 'Jugador16', 'peso': 2},
    {'nombre': 'Jugador21', 'peso': 4},
    {'nombre': 'Jugador22', 'peso': 3},
    {'nombre': 'Jugador23', 'peso': 2},
    {'nombre': 'Jugador24', 'peso': 6},
    {'nombre': 'Jugador25', 'peso': 1},
    {'nombre': 'Jugador26', 'peso': 3},
]

suma_total = sum(jugador['peso'] for jugador in jugadores)
suma_objetivo = suma_total / 3 # Suma objetivo para cada grupo

solucion = particionar_jugadores(jugadores, [], 0, suma_objetivo)

if solucion:
    for i, grupo in enumerate(solucion):
        print(f"Grupo {i+1}:")
        for jugador in grupo:
            print(f"  - {jugador['nombre']} (Peso: {jugador['peso']})")
else:
    print("No se encontró una solución que cumpla con los requisitos.")
