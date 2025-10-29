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
    if sonBarcosVálidos(barcos) and hayBarcosSuperpuestosOAdyacentes(barcos):
        for barco in barcos:
            cantidad += unoSiCeroSiNo(tamañoBarco(barco) == tamaño)

    return cantidad # TODO: Implementame
"""Duda respecto al ejercicio 1, ¿hago algo si no son barcos válidos? mensaje
al usuario? y si hay superpuestos? intenté verificarlo con la segunda 
condición del and, abajo tengo superpuestos y da cero la cantidad de Barcos de Tamaño."""
print(cantidadDeBarcosDeTamaño((
(('H', 3), ('H', 4), ('H', 5)),
(('H', 3), ('H', 4), ('H', 5)),
(('F', 4), ('E', 4)),
(('B', 4), ('B', 3), ('B', 2))), 3
))  
## Ejercicio 2

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """ Agregar docstring acá
    """
    # TODO: Implementame
    return((5,5), [3, 3, 2], [UNO],
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
    )

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



