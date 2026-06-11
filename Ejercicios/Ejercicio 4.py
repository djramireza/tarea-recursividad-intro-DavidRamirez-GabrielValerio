#E: Numero entero postivo
#S: NUmero invertido

def invertir_numero(n):
    return invertir_numero_aux(n, 0)


def invertir_numero_aux(n, res):
    if n == 0:
        return res
    return invertir_numero_aux(n//10, res * 10 + n % 10)