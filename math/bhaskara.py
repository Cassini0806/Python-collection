import math

valueA = float(input("valor de a: "))
valueB = float(input("valor de b: "))
valueC = float(input("valor de c: "))

valueD = -4 * valueA * valueC

valueF = valueB**2 + valueD
delta = math.sqrt(valueF)

valueB0 = valueB * -1

result1 = (valueB0 + float(delta)) / (2*valueA)
result2 = (valueB0 - float(delta)) / (2*valueA)

print("Resultado 1: ", result1, "Resultado 2: ", result2)
