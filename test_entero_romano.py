import pytest
from romanos_funcional import RomanNumberError, entero_a_romano, romano_a_entero

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

def test_1336():
    assert entero_a_romano(1336) == 'MCCCXXXVI'

def test_336():
    assert entero_a_romano(336) == ["CCCXXXVI"]

def test_romano_a_entero_ordenados():
    assert romano_a_entero ('I') == 1
    assert romano_a_entero ('XDCCXIII') == 1713

#Para hacer la captura del error se utiliza el ejemplo de la funcion de abajo 
def test_romano_a_entero_no_mas_de_tres():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero("LIIII")

    assert str(exceptionInfo.value) == "No se puede repetir más de tres repeticiones"

