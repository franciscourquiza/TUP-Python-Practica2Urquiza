"""Any y Sets."""

from typing import Any, Iterable

def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:  # noqa: E501
    for i in lista_1:
        for j in lista_2:
            if i == j:
                return True
    """Toma dos listas y devuelve un booleano en base a si tienen al menos 1 elemento en común.
    Restricciones:
        - Utilizar dos bucles FOR anidados.
        - Utilizar dos returns."""


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    for x, i in zip(lista_1, lista_2):
        if x == i:
            return True
    return False
    """Re-Escribir utilizando un sólo bucle y el operador IN.
    Restricciones:
        - Utilizar un único bucle FOR.
        - Utilizar dos returns.
    """


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    return True if any(lista_2) == any(lista_1) else False
    """Re-Escribir utilizando la funcion any.
    Restricciones:
        - No utilizar bucles.
        - Utilizar una comprensión.
        - La solución debe tener 1 línea.
    Referencia: https://docs.python.org/3/library/functions.html#any
    """


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    lista_1 = set(lista_1)
    lista_2 = set(lista_2)
    return (lista_1.intersection(lista_2))
    """Re-Escribir utilizando conjuntos (sets).
    Restricciones:
        - Resolver sólo utilizando operaciones de conjuntos
        - No utilizar ANY, ALL, FOR, IF ni COMPRENSIONES
    Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset  # noqa: E501
    """


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN