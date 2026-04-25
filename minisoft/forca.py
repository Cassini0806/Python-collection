from random import choice
from os import system

def nova_palavra():
    """sorteia uma palavra aleatória de uma lista""" 
    palavras = [
    "bolo", "dado", "faca", "gato", "hora", "jogo", "luta", "mesa", "nave", "ouro",
    "pato", "roda", "suco", "teia", "urso", "vela", "zero", "alvo", "belo", "cedo",
    "doce", "eixo", "fogo", "gelo", "hoje", "ilha", "juro", "lado", "mato", "neto",
    "olho", "pele", "real", "selo", "tela", "unha", "vaso", "alga", "bota", "cano",
    "dedo", "erva", "fase", "gula", "hino", "ioga", "jato", "lama", "meio", "nota",
    "odio", "pulo", "ramo", "sapo", "teto", "urna", "vida", "alma", "bico", "cena",
    "duas", "elos", "fama", "guri", "fera", "item", "joia", "lira", "muro", "neve",
    "pote", "rede", "sino", "toca", "uvas", "voto", "area", "bule", "casa", "dano",
    "este", "furo", "gado", "hugo", "indo", "jeca", "lixo", "mimo", "nulo", "obra",
    "pena", "riso", "sete", "tudo", "urge", "vila", "azul", "moca", "moda", "mula"
]
    return choice(palavras)

def rodada(palavra, texto_revelado, letras):
    """função que recebe a palavra sorteada e o input do jogador, retornando quais letras foram adivinhadas"""
    entrada = input(">>> ").lower()
    chute = entrada[0]
    letras = letras.append(chute)
    pre_texto = ""
    novo_texto = ""

#Escreve um pré-texto revelado mostrando apenas os caracters identicos na palavra original.                            
    for letra in range(len(palavra)):
        if chute == palavra[letra]:
            pre_texto += chute
        else:
            pre_texto += "-"

#Compara cada caractere do pré-texto com os do texto revelado anteriormente para soma-los. Se forem iguais e hifen, retorna hifen. Caso contrario, retorna o valor do outro caractere.
#Tabela Verdade OR, com "-" == 0 e letra == 1

#    P    R    S
#    -    -    -
#    -    L    L
#    L    -    L
#    L    L    L
                                                                                               
    for letra in range(len(palavra)):
        if pre_texto[letra] == texto_revelado[letra]:
            if pre_texto[letra] == "-":
                novo_texto += "-"
            else:
                novo_texto += pre_texto[letra]
        else:
            if pre_texto[letra] == "-":
                novo_texto += texto_revelado[letra]
            else:
                novo_texto += pre_texto[letra] 
                                                                                  
    return novo_texto

def formatacao(texto_revelado, vidas, letras):
    """formata as informações na tela"""
    
    system("clear")    
    print(f"Letras tentadas: {letras}")
    print(f"Você tem {vidas} vidas.")
    print(texto_revelado)

def main(vidas):
    """define a palavra para adivinhar e o texto revelado como uma string de hifens e roda o codigo do jogo enquanto houver vidas e a palavra não for adivinhada"""
    
    palavra = nova_palavra()
    texto_revelado = "-" * len(palavra)
    letras = []
    while True:
        formatacao(texto_revelado, vidas, letras)
        texto_revelado = rodada(palavra, texto_revelado, letras)
        if palavra == texto_revelado:
            print("Você Ganhou :D")
            print(f"A palavra era '{palavra}'.")
            break
        else: 
            vidas -= 1
            if vidas == 0:
                print("Você Perdeu :(")
                print(f"A palavra era '{palavra}'.")
                break     
                                  
main(10)