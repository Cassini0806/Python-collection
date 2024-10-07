value1 = float(input("valor 1: "))
operador = input("Operador: ")
value2 = float(input("valor 2: "))

def Calculadora():
    operadores = ['+', '-', '*', '/']
    
    if operador == operadores[0]:
        value3 = value1 + value2
        print(value1, operador, value2, "=", value3)
    elif operador == operadores[1]:
        value3 = value1 - value2
        print(value1, operador, value2, "=", value3)
    elif operador == operadores[2]:
        value3 = value1 * value2
        print(value1, operador, value2, "=", value3)
    elif operador == operadores[3]:
        value3 = value1 / value2
        print(value1, operador, value2, "=", value3)
    else:
        print("Operador não identificado")

Calculadora()