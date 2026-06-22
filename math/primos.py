primos = [] 

def eh_primo(n):
    global primos
    if len(primos) > 0:
        for num in primos:
            if n % num == 0:
                return False
        return True
    elif n == 2:
        return True
    else:
        return False

def dicio_primos():
    global primos
    valor_max = int(input("Calcular primos de 0 até "))
    for i in range(1, valor_max+1):
        if eh_primo(i) == True:
            primos.append(i)
    return primos

print(dicio_primos())
