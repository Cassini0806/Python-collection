def busca(lista):
    if len(lista) == 0:
        return None #Retorna None se a lista estiver vazia

    big = lista[0]
    for i in lista:
        if big < i:
            big = i
    return big

lista = [23, 57, 91, 14, 36, 78, -501, 66, 57, 89]
maior = busca(lista)
print(maior)