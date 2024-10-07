def bubble(lista):
    lenght = len(lista)
    for i in range(lenght):
        troca = False
        for j in range(0, lenght - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                troca = True
        if not troca:
            break
    return lista

lista = [6,5,2,9,7]
listor = bubble(lista)
print(listor)
