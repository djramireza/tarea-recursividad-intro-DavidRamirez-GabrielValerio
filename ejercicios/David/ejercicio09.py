#ejercicio 9

def sublistas_ascendentes(lista, actual = None, resultado=None):
    if resultado is None:
        resultado = []
    if actual is None:
        actual = []
        
    if not lista:
        if actual:
            resultado.append(actual)
        return resultado

    if not actual:
        actual = [lista[0]]
        return sublistas_ascendentes(lista[1:], actual, resultado)
    
    if lista[0] > actual[-1]:
        actual.append(lista[0])
        return sublistas_ascendentes(lista[1:], actual, resultado)

    else:
        resultado.append(actual)
        return sublistas_ascendentes(lista[1:], [lista[0]], resultado)
