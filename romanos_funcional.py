#Versión de Romano a entero de Enric

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


def entero_a_romano(numero):
    numero = "{:0>4d}".format(numero)
    digitos = list(numero)

    longitud = len(digitos)
    romano = ''
    for ix in range(len(numero)):
        longitud -= 1
        digitos[ix] = digitos[ix] + "0" * longitud
        romano += componentes.get(int(digitos[ix]), "")

    return romano


simbolos_romanos = {"M":1000, "D":500,"C":100, "L":50, "X":10,"V":5, "I":1, "": 0}

class RomanNumberError(Exception):
    pass


def romano_a_entero(romano: str) -> int:
    res = 0
    #contador para ver cuántas veces seguidas se repite el caracter
    contador_rep = 1
    #variable para guardar el caracter
    car_anterior = ''
    #recoremos el caractaer y se compara con el anterior si coincide se suma en el contador
    for caracter in romano:
        if caracter == car_anterior:
            contador_rep += 1
        #Si no coincide se pone de nuevo contador a 1
        else:
            contador_rep = 1
        #rompemos el for si el contador pasa de 3
        if contador_rep > 3:
            raise RomanNumberError("No se puede dar más de tres repeticiones")
            #Comparamos si caracter actual es mayor que caracter anterior para restar
        if simbolos_romanos[caracter] > simbolos_romanos[car_anterior]:
            r -= simbolos_romanos[car_anterior]*2
        #recordamos el caracter anterior
        res += simbolos_romanos[caracter]
        car_anterior = caracter 
        
    return res