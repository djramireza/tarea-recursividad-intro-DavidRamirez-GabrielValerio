#E: lista de enteros 
#S: lista de listas con las secuencias de 3 elementos seguidos donde el central sea el menor

def detectar_valles(lista):
    if len(lista) < 3:
        return []

    anterior = lista[0]
    actual = lista[1]
    sig = lista[2]

    if actual < anterior and actual < sig:
        return [[anterior, actual, sig]] + detectar_valles(lista[1:])
    else:
        return detectar_valles(lista[1:])

