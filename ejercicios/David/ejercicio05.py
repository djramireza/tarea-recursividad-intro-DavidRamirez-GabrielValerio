#ejercicio 5

def eliminar_impares(num, resultado = 0, exp=0):
    if num == 0:
        return resultado
    nuevo = num % 10
    if nuevo % 2 == 0:
        resultado += nuevo * (10 ** exp)
        exp+=1
        
    return eliminar_impares(num//10, resultado, exp)
        
