"""
1º Crear una función que pase de entero > 0 y <4000 a Romano
2º Cualquier otra entrada debe de dar error.

Casos de prueba:

a)1994 -> MCMXCIV
b)4000 -> RomanNumberError (El número es mayor a 3994)
c)"una cadena" -> RomanNumberError (Debe ser un entero)
d)0 -> RomanNumberError (El valor debe ser superior a 0)
e)-3 -> RomanNumberError (El valor debe de ser positivo)
f)4.5 -> RomanNumberError(No pongas números decimales,deben ser enteros)
"""


class RomanNumberError(Exception):
    pass

numero_romano = [
    (1000, "M"),(500, "D"),(100, "C"),(50, "L"),(10, "X"), (5, "V"),(1, "I")

]

def entero_a_romano(numero):
    numero = str(numero)
    longitud = len(numero)

    if longitud < 4:
        numero = "{:0>4s}".format(numero)
    
    digitos = list(numero)

    ix = 0
    longitud = 4
    for n in numero:
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        ix += 1
    return digitos