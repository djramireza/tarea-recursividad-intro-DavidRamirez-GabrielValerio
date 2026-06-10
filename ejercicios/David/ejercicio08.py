#ejercicio 8

def detectar_valles(lista):
    return detectar_valles_aux(lista)

def detectar_valles_aux(lista, resultado = None, i =1, valles=[]):
    if resultado is None:
        resultado = []
    if i >= len(lista)-1:
        return resultado
    
    if lista[i] < lista[i-1] and lista[i] < lista[i+1]:
        resultado.append([lista[i-1],lista[i], lista [i+1]])
    
    return detectar_valles_aux(lista, resultado, i+1)
    
