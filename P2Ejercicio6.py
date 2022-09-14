"""Type, Comprensión de Listas, Sorted y Filter."""

from cmath import e
from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    lista1 = []
    listaletras = []
    listanumeros = []
    for i in lista:
        if type(i) == str:
            listaletras.append(i)
        else:
            listanumeros.append(i)
    lista1.extend(listaletras)
    lista1.extend(listanumeros)
    return (lista1)
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    lista1 = []
    listaletras = []
    listanumeros = []
    for i in lista:
        if type(i) == str:
            listaletras.append(i)
        else:
            listanumeros.append(i)
    lista1.extend(listaletras)
    lista1.extend(listanumeros)
    return (lista1)
    """Re-escribir utilizando comprensión de listas.
    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10] # noqa: E501
# NO MODIFICAR - FIN