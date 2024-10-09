lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, j in enumerate(lista):
    n = i/2
    if n == int(n):
        n = 'impar'
    else:
        n = 'par'
    print(j, n)

#abaixo a versão que o chatoGPT criou (ele subestima de minha capacidade ¬_¬ )
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#for j in lista:
#    if j % 2 == 0:
#        n = 'par'
#    else:
#        n = 'impar'
#    print(j, n)
