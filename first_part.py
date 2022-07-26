"""
1. Crear una función que pase de entero > 0 y < 4000 a romano
2. Cualquier otra entrada debe dar error
"""

class RomanNumberError(Exception):
    pass

numero_romano = (
    (1000, 'M'), (500, 'D'), (100, 'C'), (50, 'D'), (10, 'X'), (5, 'V'), (1, 'I')
)
"""
#Versión Victor:
millares = ((1000, 'M'), (2000, 'MM'), (3000, 'MMM')) 

centenas = ((100, 'C'), (200, 'CC'), (300, 'CCC'),
        (400, 'CD'), (500, 'D'), (600, 'DC'),
        (700, 'DCC'), (800, 'DCCC'), (900, 'CM'))

decenas = ((10, 'X'), (20, 'XX'), (30, 'XXX'),
        (40, 'XL'), (50, 'L'), (60, 'LX'),
        (70, 'LXX'), (80, 'LXXX'), (90, 'XC'))
    
unidades = ((1, 'I'), (2, 'II'), (3, 'III'),
        (4, 'IL'), (5, 'V'), (6, 'VI'),
        (7, 'VII'), (8, 'VIII'), (9, 'IX'))

def entero_a_romano(numero):

    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    ix = 0
    longitud = 4

    for n in numero:
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        ix += 1

    traduccion = []

    for m in millares:
        if digitos [0] == str(m[0]):
            traduccion.append(m[1])
            break

    for c in centenas:
        if digitos [1] == str (c[0]):
            traduccion.append(c[1])
            break

    for d in decenas:
        if digitos [2] == str (d[0]):
            traduccion.append(d[1])
            break
    
    for u in unidades:
        if digitos [3] == str (u[0]):
            traduccion.append(u[1])
            break

    return "".join(traduccion)

valor = int(input("Introduce un número entero y te lo devolverá en Romano: "))
print(entero_a_romano(valor))
"""


numero_romano = {
    1000: 'M', 500: 'D', 100: 'C', 50: 'D', 10: 'X', 5: 'V', 1: 'I'
}

algoritmo_romano = (
    {1: 'M'},
    {1: 'C', 5: 'D', 10: 'M'},
    {1: 'X', 5: 'L', 10: 'C'},
    {1: 'I', 5: 'V', 10: 'X'},
)


componentes = {
    1000: 'M', 2000: 'MM', 3000: 'MMM', 
    100: 'C', 200: 'CC', 300: 'CCC',
    400: 'CD', 500: 'D', 600: 'DC',
    700: 'DCC', 800: 'DCCC', 900: 'CM',
    10: 'X', 20: 'XX', 30: 'XXX',
    40: 'XL', 50: 'L', 60: 'LX',
    70: 'LXX', 80: 'LXXX', 90: 'XC',
    1: 'I', 2: 'II', 3: 'III',
    4: 'IL', 5: 'V', 6: 'VI',
    7: 'VII', 8: 'VIII', 9: 'IX'
}    


def entero_a_romano_2(numero):
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    romano = ''

    for tipo_unidad, digito in enumerate(digitos):
        digito = int(digito)
        tupla_activa = algoritmo_romano[tipo_unidad]

        if digito < 4:
            romano += tupla_activa[1] * digito
        elif digito == 4:
            romano += tupla_activa[1] + tupla_activa[5]
        elif int(digitos[1]) < 9:
            romano += tupla_activa[5] + tupla_activa[1] * (digito - 5)
        else:
            romano += tupla_activa[1] + tupla_activa[10]

    return romano


def entero_a_romano(numero):
    """
    numero = str(numero)
    longitud = len(numero)

    if longitud < 4:
        numero = "{:0>4s}".format(numero)
    """
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    longitud = len(digitos)
    romano = ''
    for ix in range(len(numero)):
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        romano += componentes.get(int(digitos[ix]), "")

    return romano