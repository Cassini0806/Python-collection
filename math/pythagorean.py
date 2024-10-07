import math

value1 = float(input("Cateto Oposto: "))
value2 = float(input("Cateto Adjacente: "))

def pythagoras():
    value3 = (value1**2) + (value2**2)
    value4 = math.sqrt(value3)
    return float(value4)

print("Hipotenusa: ", pythagoras())
