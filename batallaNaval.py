from typing import Any
from biblioteca import *

## Ejercicio 1

def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """ 
    Indica cuantos barcos de tamaño *tamaño* hay entre los BarcosVálidos
    
    PRE:
        los barcos son válidos {sonBarcosVálidos(barcos)}

    ARGS:
        barcos (list[BarcoEnGrilla]): Los barcos válidos colocados en la grilla.
    
    RETURNS:
        cantidad de barcos de tamaño *tamaño* en barcos
    """
    cantidad:int = 0
    for barco in barcos:
        cantidad += unoSiCeroSiNo(tamañoBarco(barco) == tamaño)
    return cantidad

## Ejercicio 2

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:

    """
    Arma un juego nuevo con tableros de Dimensiones *cantidadDeFilas* X *cantidadDeColumnas*
    con los barcos válidos *barcosDisponibles*, y dos tableros VACÍOS para los dos jugadores.
    PRE: 
        las dimensiones son válidas: {cantidadDeFilasVálida} cantidadDeColumnas >= 1
        la cantidad de barcos es válida {len(barcosDisponibles) > 0}

    ARGS:
        cantidadDeFilas (int): la cantidad de filas que va a tener la grilla
        cantidaDeColumnas (int): la cantidad de columnas que va a tener la grilla
        barcosDisponibles (list[barco]): los barcos que hay que colocar.
    RETURNS:
        Un Tableros válidos, uno para cada jugador y los barcos disponibles para colocar.

    """
    
    tablero_jugador_uno: Tablero = nuevoTablero(cantidadDeFilas, cantidadDeColumnas)
    tablero_jugador_dos: Tablero = nuevoTablero(cantidadDeFilas, cantidadDeColumnas)
    return ((cantidadDeFilas, cantidadDeColumnas),
            barcosDisponibles,
            jugadorQueEmpieza(),
            tablero_jugador_uno,
            tablero_jugador_dos)


def crearGrillaVacía(cantidadDeFilas:int, cantidadDeColumnas:int) -> Grilla:
    i_fila:int = 0
    i_columna:int = 0
    grilla_nueva: Grilla = []
    for i_fila in range(cantidadDeFilas):
        grilla_nueva.append([])
        for i_columna in range(cantidadDeColumnas):
            grilla_nueva[i_fila].append(VACÍO)
    return grilla_nueva

def nuevoTablero(cantidadDeFilas:int, cantidadDeColumnas:int) -> Tablero:
    tableroNuevo:Tablero = (crearGrillaVacía(cantidadDeFilas, cantidadDeColumnas),
                            crearGrillaVacía(cantidadDeFilas, cantidadDeColumnas))
    return tableroNuevo
















































## Ejercicio 3

def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """ Agregar docstring acá
    """
    return False # TODO: Implementame


## Ejercicio 4

def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """ Agregar docstring acá
    """
    return NADA # TODO: Implementame


## Ejercicio 5

def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """ Agregar docstring acá
    """
    return [] # TODO: Implementame



