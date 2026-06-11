#E: Una lista
#S: El numero mayor de esa lista

def mayor_lista(lista):
    if len(lista) == 1:
        return lista[0]
    primero = lista[0]
    mayor_resto = mayor_lista(lista[1:])
    if primero > mayor_resto:
        return primero
    else:
        return mayor_resto
    


    