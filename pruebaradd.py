"""from romano_class import NumeroRomano,RomanNumberError



def __radd__(self, otro):
        if len(self) != len(otro):
            raise RomanNumberError
            
        return NumeroRomano([x+y for x,y in zip(self, otro)])
        
prueba = NumeroRomano([1, 2, 3])
print(prueba * 3)
print(prueba * NumeroRomano([4, 5 ,6]))
NumeroRomano([3, 6, 9])
NumeroRomano([4, 10, 18])"""




class Vector(list):   
    def __add__(self, other):
        if len(self) != len(other):
            raise "prueba"
            
        return Vector([x+y for x,y in zip(self, other)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector([x*y for x,y in zip(self, other)])
        
        return Vector([x*other for x in self])
    
    def __repr__(self):
        return "Vector({})".format(list.__repr__(self))
    
v1 = Vector([1, 2, 3])
print(v1 * 3)
print(v1 * Vector([4, 5 ,6]))
Vector([3, 6, 9])
Vector([4, 10, 18])