import random

number = random.randint(1, 10)

tent = 0
advi = False

while not advi:
    palpite  = int(input("Adivinhe um número entre 1 e 10: "))
    tent += 1

    if palpite == number:
        advi = True
        print("voce acertou")
    else:
        print("voce errou")
        

    cont = input("Deseja contiuar? (S/N): ")

    if cont.lower()  == 'S' or 's':
        number = random.randint(1, 100)
        tent = 0
        advi = False
    else:
        print("Obrigado por jogar")
    break
