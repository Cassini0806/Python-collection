def fibonacci(n):
    lista = []
    a, b = 0, 1
    for i in range(n):
        lista.append(a)
        a, b = b, a + b            
    return lista

n = input("Número de elementos desejados: ")
print(fibonacci(n))