#Recebe o número a ser convertido, cria lista para ordenar elementos e string para formata-los
n = int(input("> "))
bin = []
text = ""
#calcula o valor em binário pelo resto de sucessivas divisões e adiciona em bin
while n >= 2:
	d = n%2
	n = int(n / 2)
	bin.insert(0, d)
bin.insert(0, n)
#transforma a lista bin em um texto para melhor leitura e imprime na tela
for i in range(len(bin)):
	text += str(bin[i])
print(text)

