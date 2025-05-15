"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

from DataStructures.Utils import config
from DataStructures.Utils import error as error
from DataStructures.List import list as lt
assert config
from DataStructures.List import single_linked_list as slt

"""
  Este módulo implementa el tipo abstracto de datos pila
  (Stack) sobre una lista encadenada.
"""


def new_stack(cmpfunction=None, module='SINGLE_LINKED', key=None, filename=None, delim=','):
    """ Crea una pila vacía.

    Args:
        cmpfunction: Función de comparación (opcional)
        module: Indica el tipo de estructura de datos a utilizar para implementar la pila
        key: Clave para la lista (opcional)
        filename: Nombre del archivo (opcional)
        delim: Delimitador para el archivo CSV (opcional)
    Returns:
        Una pila vacía
    Raises:
        Exception
    """
    try:
        return slt.new_list(cmpfunction, module, key, filename, delim)
    except Exception as exp:
        error.reraise(exp, 'TADStack->newStack: ')


def push(stack, element):
    """ Agrega el elemento element en el tope de la pila.

    Args:
        stack:  La pila donde se insetará el elemento
        element:  El elemento a insertar

    Returns:
        La pila modificada

    Raises:
        Exception
    """
    try:
        slt.add_last(stack, element)
        return stack
    except Exception as exp:
        error.reraise(exp, 'TADStack->Push: ')


def pop(stack):
    """ Retorna el elemento  presente en el tope de la pila.

     Args:
        stack:  La pila de donde se retirara el elemento

    Returns:
        El elemento del tope de la pila

    Raises:
        Exception
    """
    try:
        if stack is not None and not slt.is_empty(stack):
            return slt.remove_last(stack)
        else:
            raise Exception
    except Exception as exp:
        error.reraise(exp, 'TADStack->pop: ')


def is_empty(stack):
    """Informa si la pila es vacía o no
     Args:
        stack:  La pila a examinar

    Returns:
        True si la pila es vacia
        False de lo contrario

    Raises:
        Exception
    """
    try:
        return slt.is_empty(stack)
    except Exception as exp:
        error.reraise(exp, 'TADStack->isEmpty: ')


def top(stack):
    """ Retorna el elemento en tope de la pila, sin eliminarlo de la pila

    Args:
        stack:  La pila a examinar

    Returns:
        El primer elemento de la pila, sin eliminarlo

    Raises:
        Exception
    """
    try:
        return slt.last_element(stack)
    except Exception as exp:
        error.reraise(exp, 'TADStack->top: ')


def size(stack):
    """ Informa el número de elementos en la pila
    Args:
        stack: La pila a examinar

    Returns:
        Retorna el tamaño de la pila

    Raises:
        Exception
    """
    try:
        return slt.size(stack)
    except Exception as exp:
        error.reraise(exp, 'TADStack->size: ')