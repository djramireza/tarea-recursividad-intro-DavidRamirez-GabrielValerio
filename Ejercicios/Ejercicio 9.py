#E: Lista de numeros enteros 
#S: Lista de sublistas con secuencia de numeros consecutivos estrictamente ascendentes

def sublistas_ascendentes(lista):
    if not lista:
        return []
    return ascendentes_aux(lista[1:], [lista[0]], [])

def ascendentes_aux(lista, sublista, res):
    if not lista:
        return res + [sublista]

    if lista[0] > sublista[-1]:
        return ascendentes_aux(lista[1:], sublista + [lista[0]], res)
    else: 
        return ascendentes_aux(lista[1:], [lista[0]], res + [sublista])

