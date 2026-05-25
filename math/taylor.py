import math

def exponential(x: float, termos: int):
    """exponential(x: float, termos: int)
    Calcula a exponencial de 'e' utilizando a série de Taylor.
    >>> exponential(0.5, 5)
    1.6484375
    """
    exp = 0 #variavel da soma de termos
    i = 0 #indice que enumera o termo atual
    while i < termos:
        exp += math.pow(x, i) / math.factorial(i)       
        i += 1
    return exp

if __name__ == '__main__':
    import doctest
    doctest.testmod()
