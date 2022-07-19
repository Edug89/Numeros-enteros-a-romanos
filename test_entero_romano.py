from first_part import entero_a_romano

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

def test_3_es_igual_2_mas_1():
    assert 2 + 1 == 3

def test_descomposicion_336():
    assert entero_a_romano() == ["0000", "300", "30", "6"]


