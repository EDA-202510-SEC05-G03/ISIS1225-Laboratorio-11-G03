from DataStructures.Map import map_linear_probing as map
from DataStructures.Graph import vertex as V

def new_graph(order):
    """
    Crea un grafo dirigido vacío.

    Parameters
    ----------
    order : int
        Número inicial de vértices (tamaño de la tabla de hashing).

    Returns
    -------
    dict
        Grafo recién creado con:
          - 'vertices': mapa lineal probing
          - 'num_edges': 0
    """
    return {
        'vertices': map.new_map(order, 0.5),
        'num_edges': 0
    }
    
def insert_vertex(my_graph, key_u, info_u):
    vertex = V.new_vertex(key_u, info_u)
    map.put(my_graph['vertices'], key_u, vertex)
    return my_graph


def update_vertex_info(my_graph, key_u, new_info_u):
    """
    Actualiza la información del vértice key_u con new_info_u.

    Parameters
    ----------
    my_graph : dict
        Grafo sobre el que se opera.
    key_u : any
        Llave del vértice a actualizar.
    new_info_u : any
        Nueva información asociada al vértice.

    Returns
    -------
    dict or None
        Si el vértice no existe, devuelve None.
        Si existe, actualiza y devuelve el grafo.
    """
    v = map.get(my_graph['vertices'], key_u)
    if v is None:
        return None
    # Modificamos directamente el diccionario del vértice
    v['value'] = new_info_u
    # Re-escribimos la entrada en el mapa para asegurar consistencia
    map.put(my_graph['vertices'], key_u, v)
    return my_graph

def remove_vertex(my_graph, key_u):
    """
    Elimina el vértice key_u y todos sus arcos asociados.

    Parameters
    ----------
    my_graph : dict
        Grafo sobre el que se opera.
    key_u : any
        Llave del vértice a eliminar.

    Returns
    -------
    dict or None
        Si el vértice no existe, devuelve None.
        Si existe, elimina vértice y arcos y devuelve el grafo.
    """
    # 1) Obtener el vértice y su lista de salientes
    v = map.get(my_graph['vertices'], key_u)
    if v is None:
        return None

    # 2) Contar y eliminar sus aristas salientes
    out_count = map.size(v['adjacents'])
    # quitar el vértice del grafo
    map.remove(my_graph['vertices'], key_u)
    my_graph['num_edges'] -= out_count

    # 3) Eliminar todas las aristas entrantes hacia key_u
    #    Recorremos UNA VEZ la lista de claves restantes
    for other_key in map.keys(my_graph['vertices']):
        other_v = map.get(my_graph['vertices'], other_key)
        removed = map.remove(other_v['adjacents'], key_u)
        if removed is not None:
            my_graph['num_edges'] -= 1

    return my_graph

def add_edge(my_graph, key_u, key_v, weight=1.0):
    """
    Agrega un arco dirigido de key_u a key_v, con peso opcional.

    Si alguno de los vértices no existe, lanza Exception.
    Si el arco ya existe, actualiza su peso (no paralelos).

    Parameters
    ----------
    my_graph : dict
        Grafo sobre el que se opera.
    key_u : any
        Vértice de origen.
    key_v : any
        Vértice destino.
    weight : float, optional
        Peso del arco (por defecto 1.0).

    Returns
    -------
    dict
        El grafo con el arco agregado o modificado.

    Raises
    ------
    Exception
        Si key_u no existe: "El vertice u no existe"
        Si key_v no existe: "El vertice v no existe"
    """
    src = map.get(my_graph['vertices'], key_u)
    if src is None:
        raise Exception("El vertice u no existe")
    dst = map.get(my_graph['vertices'], key_v)
    if dst is None:
        raise Exception("El vertice v no existe")

    adj = src['adjacents']
    existing = map.get(adj, key_v)
    if existing is None:
        # Arista nueva
        e = V.new_edge(key_u, key_v, weight)
        V.add_adjacent(src, key_v, e)
        my_graph['num_edges'] += 1
    else:
        # Reemplazamos sólo el peso
        existing['weight'] = weight
        map.put(adj, key_v, existing)

    return my_graph

def order(my_graph):
    """
    Retorna el orden del grafo: número de vértices.
    """
    return map.size(my_graph['vertices'])

def size(my_graph):
    """
    Retorna el tamaño del grafo: número de aristas.
    """
    return my_graph['num_edges']

def vertices(my_graph):
    """
    Retorna una lista con las llaves de los vértices del grafo.

    Parameters
    ----------
    my_graph : dict
        Grafo sobre el que se opera.

    Returns
    -------
    list
        Lista de llaves de los vértices.
    """
    return map.key_set(my_graph['vertices'])

def degree(my_graph, key_u):
    """
    Retorna el grado del vértice key_u.

    Parameters
    ----------
    my_graph : dict
        Grafo sobre el que se opera.
    key_u : any
        Llave del vértice.

    Returns
    -------
    int
        Grado del vértice.
    """
    v = map.get(my_graph['vertices'], key_u)
    if v is None:
        return None
    return map.size(v['adjacents'])

