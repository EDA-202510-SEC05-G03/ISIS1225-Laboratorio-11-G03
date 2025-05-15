import sys
import os

# Agrega el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from DataStructures.List import array_list as slt
from DataStructures.Utils import error

def new_queue(cmpfunction=None, module='SINGLE_LINKED', key=None, filename=None, delim=','):
    """ Crea una cola vacía.

    Args:
        cmpfunction: Función de comparación (opcional)
        module: Indica el tipo de estructura de datos a utilizar para implementar la cola
        key: Clave para la lista (opcional)
        filename: Nombre del archivo (opcional)
        delim: Delimitador para el archivo CSV (opcional)
    Returns:
        Una cola vacía
    Raises:
        Exception
    """
    try:
        return slt.new_list(cmpfunction, module, key, filename, delim)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->newQueue: ')

def enqueue(queue, element):
    """Agrega el elemento element en el tope de la pila
    Args:
        queue: La cola donde se insertará el elemento
        element:  El elemento a insertar

    Returns:
        La cola modificada
    Raises:
        Exception
    """
    try:
        slt.add_last(queue, element)
        return queue
    except Exception as ex:
        error.reraise(ex, 'enqueue ')

def dequeue(queue):
    """ Retorna el elemento en la primer posición de la cola, y lo elimina.
     Args:
        queue: La cola donde se eliminará el elemento

    Returns:
        El primer elemento de la cola
    Raises:
        Exception
    """
    try:
        return slt.remove_first(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->dequeue: ')

def peek(queue):
    """ Retorna el elemento en la primer posición de la cola sin eliminarlo
    Args:
        queue: La cola  a examinar

    Returns:
        True el primer elemento de cola sin eliminarlo
    Raises:
        Exception
    """
    try:
        return slt.first_element(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->peek: ')

def is_empty(queue):
    """Informa si la cola es vacía o no
    Args:
        queue: La cola  a examinar

    Returns:
        True si la cola es vacia, False de lo contrario
    Raises:
        Exception
    """
    try:
        return slt.is_empty(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->isEmpty: ')

def size(queue):
    """Informa el número de elementos en la cola
    Args:
        queue: La cola  a examinar

    Returns:
        Retorna el tamaño de la cola

    Raises:
        Exception
    """
    try:
        return slt.size(queue)
    except Exception as exp:
        error.reraise(exp, 'TADQueue->size: ')