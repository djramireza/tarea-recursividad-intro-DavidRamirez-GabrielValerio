#Ejercicio 2
def contar_pares(num):
    return contar_pares_aux(num, 0)

def contar_pares_aux(num, resultado):
    if num == 0:
        return resultado
    
    nuevo = num %10
    
    if nuevo%2 == 0:
        resultado += 1
    return contar_pares_aux(num//10, resultado)
        
