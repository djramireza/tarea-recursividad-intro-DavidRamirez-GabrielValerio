#E: Una lista de enteros
#S: Lista de listas, cada sublista tiene numero y cantidad de veces que aparece

def comprimir_repetidos(lista):
    if not lista:
        return []
    return comprimir_aux(lista)

def comprimir_aux(lista):
    if len(lista) == 1:
        return [[lista[0], 1]]
    
    resultado_restante = comprimir_aux(lista[1:])
    
    primer_grupo = resultado_restante[0]
    
    if lista[0] == primer_grupo[0]:
        primer_grupo[1] += 1
        return resultado_restante
    else:
        return [[lista[0], 1]] + resultado_restante