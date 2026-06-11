#E: Lista de numeros
#S: cantidad de bloques de numeros iguales consecutivos

def contar_bloques_iguales(lista):
    if not lista:
        return 0
    return iguales_aux(lista[1:], lista[0], 1)

def iguales_aux(lista, anterior, cont):
    if not lista:
        return cont

    if lista[0] != anterior:
        return iguales_aux(lista[1:], lista[0], cont+1)
    else:
        return iguales_aux(lista[1:], lista[0], cont)


    

