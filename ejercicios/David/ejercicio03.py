#ejercicio 3

def mayor_lista(lista):
    return mayor_lista_aux(lista, 0)

def mayor_lista_aux(lista, nuevo):
    if lista == []:
        return nuevo
    for num in lista:
        if num > nuevo:
            nuevo = num
    return mayor_lista_aux(lista[1:], nuevo)
