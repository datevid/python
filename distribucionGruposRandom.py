import random
def getInfoPlayers(jugadores,numEquipos):
    print("--------INFO-------")
    #total jugadores
    print("totalJugadores:{}".format(len(jugadores)))

    #numero de equpos
    print("numEquipos:{}".format(numEquipos))


    # Calcula la cantidad de jugadores por equipo
    jugadores_por_equipo = len(jugadores) // numEquipos
    print("jugadores_por_equipo:{}".format(jugadores_por_equipo))

    # Calcula la suma total de los pesos de los jugadores
    suma_pesosJugadores = sum(jugador['peso'] for jugador in jugadores)
    print("suma_pesosJugadores:{}".format(suma_pesosJugadores))


    # Calcular la media de pesos por equipo
    mediaPesosXEquipo = suma_pesosJugadores / numEquipos
    print("mediaPesosXEquipo:{}".format(mediaPesosXEquipo))
    

def getMediaPesosXEquipo(jugadores,numEquipos):
    # Calcula la suma total de los pesos de los jugadores
    suma_pesosJugadores = sum(jugador['peso'] for jugador in jugadores)
    #print("suma_pesosJugadores:{}".format(suma_pesosJugadores))


    # Calcular la media de pesos por equipo
    mediaPesosXEquipo = suma_pesosJugadores / numEquipos
    #print("mediaPesosXEquipo:{}".format(mediaPesosXEquipo))

    return mediaPesosXEquipo;

def generarGrupoRandom(jugadores,numEquipos):

	# Ordena la lista de jugadores de manera aleatoria
    random.shuffle(jugadores)
    #print("jugadores:{}".format(jugadores))

    # Lista de equipos vacía
    equipos = [[] for _ in range(numEquipos)]
    

    index=0
    for jugador in jugadores:
        equipos[index].append(jugador)
        index= (index+1)%numEquipos

    
    return equipos;

def imprimirEquipos(equipos):
    #print("equipos:{}".format(equipos))
    print("--------equipos-------")
    for i, equipo in enumerate(equipos):
        print(f"Equipo {i + 1}:")
        print("equipo: {} \n".format(equipo))
        #for jugador in equipo:
        #    print(jugador['nombre'])
        suma_pesos_equipo = sum(jugador['peso'] for jugador in equipo)
        print(f"Suma de pesos: {suma_pesos_equipo}\n")

def validaDistribucionPlayers(equipos,mediaPesosXEquipo,umbralPesos):
    print("--------validaDistribucionPlayers-------")
    print("umbralPesos: {}".format(umbralPesos))
    numEquipos=len(equipos)
    print("numEquipos: {}".format(numEquipos))
    validaDistribucionPlayers=True;
    for i, equipo in enumerate(equipos):
        print(f"Equipo {i + 1}: {equipo}")
        suma_pesos_equipo = sum(jugador['peso'] for jugador in equipo)
        print(f"mediaPesosXEquipo: {mediaPesosXEquipo}")
        print(f"peso obtenido del equipo: {suma_pesos_equipo}")
        print("diferencia pesosXEquipo obtenido: {}".format(abs(suma_pesos_equipo-mediaPesosXEquipo)))
        if(abs(suma_pesos_equipo-mediaPesosXEquipo)>umbralPesos):
            print("Se escapa del umbralPesos {}\n".format(umbralPesos))
            validaDistribucionPlayers= False
        else:
            print("Se encuentra dentro del umbralPesos {}\n".format(umbralPesos))
    
    return validaDistribucionPlayers



def distribuirEquiposFuerzaBruta(equipos,mediaPesosXEquipo,umbralPesos):
    validaDistribucionPlayersBool=False
    iteracionesFuerzaBrutaMax=50000
    iteracionesFuerzaBrutaIndex=1;
    while validaDistribucionPlayersBool is False and iteracionesFuerzaBrutaIndex<=iteracionesFuerzaBrutaMax:
        print("iteracion {}".format(iteracionesFuerzaBrutaIndex))
        validaDistribucionPlayersBool=validaDistribucionPlayers(equipos,mediaPesosXEquipo,umbralPesos)
        print("validaDistribucionPlayersBool: {}".format(validaDistribucionPlayersBool))
        iteracionesFuerzaBrutaIndex=iteracionesFuerzaBrutaIndex+1


# Ejemplo de uso
jugadores = [
    {'nombre': 'Jugador1', 'peso': 5},
    {'nombre': 'Jugador2', 'peso': 2},
    {'nombre': 'Jugador3', 'peso': 3},
    {'nombre': 'Jugador4', 'peso': 1},
    {'nombre': 'Jugador5', 'peso': 4},
    {'nombre': 'Jugador6', 'peso': 4},


    {'nombre': 'Jugador11', 'peso': 3},
    {'nombre': 'Jugador12', 'peso': 5},
    {'nombre': 'Jugador13', 'peso': 6},
    {'nombre': 'Jugador14', 'peso': 2},
    {'nombre': 'Jugador15', 'peso': 1},
    {'nombre': 'Jugador16', 'peso': 2},

    {'nombre': 'Jugador21', 'peso': 4},
    {'nombre': 'Jugador22', 'peso': 3},
    {'nombre': 'Jugador23', 'peso': 2},
    {'nombre': 'Jugador24', 'peso': 6},
    {'nombre': 'Jugador25', 'peso': 1},
    {'nombre': 'Jugador26', 'peso': 3},
    
]

numEquipos=3
umbralPesos=3
getInfoPlayers(jugadores,numEquipos);
equipos=generarGrupoRandom(jugadores,numEquipos);
mediaPesosXEquipo=getMediaPesosXEquipo(jugadores,numEquipos)
distribuirEquiposFuerzaBruta(equipos,mediaPesosXEquipo,umbralPesos)


