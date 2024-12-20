import os

#Prepara o setup com as informações primárias para executar o programa
gabarito = []
alunos = {}

nprovas = int(input("Insira o número de provas: "))
nquest = int(input("Insira o número de questões: "))
#value = int(input("Insira o valor de cada questão: "))

def definirGabarito():
    print("Por favor insira o gabarito: ")
    for i in range(nquest):
        questao = input(f"Questão {i + 1}: ")
        gabarito.append(questao)
    print(gabarito)

def inserirnotas():
    for i in range(nprovas):
        nome = input("Digite o nome do aluno: ")
        alunos[nome] = []  
        for j in range(nquest):
            ncor = 0 
            resposta = input(f"Resposta questão {j + 1}: ")
            alunos[nome].append(resposta)
        for x, y in zip(alunos[nome], gabarito):
            if x == y:
                ncor += 1
        nota = float(ncor / nquest)
        print(nota)
        alunos[nome].append(nota)
                

def exibirNotas():
    #Limpa o terminal para maior visibilidade
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS e Linux
        os.system('clear')
    print(f"Resultado Geral:")
    print(f"Gabarito: {gabarito}")
    for nome, elementos in alunos.items():
        print(f"{nome}: {elementos[:-1]} // Nota: {alunos[nome][-1]}")

definirGabarito()
inserirnotas()
exibirNotas()