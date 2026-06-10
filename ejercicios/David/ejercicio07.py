# ejercicio 7

def separar_por_paridad(num, resultado=0, pares = 0, impares = 0, exp_par = 0, exp_impar = 0):
    if num == 0:
        return resultado
    nuevo = num % 10
    if nuevo % 2 == 0:
        pares += nuevo * (10**exp_par)
        exp_par+=1

    if nuevo % 2 != 0:
        impares += nuevo * (10**exp_impar)
        exp_impar += 1
        
    resultado = [pares, impares]

    return separar_por_paridad(num//10, resultado, pares, impares, exp_par, exp_impar)

    
    
