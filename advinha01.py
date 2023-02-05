from random import randint

numeroSorte = randint(1, 10)

controlo = True
totalTentativas = 3
qtdadeTentativas = 0

while controlo:
    numEscolhido = int(input("Introduz um número! "))

    qtdadeTentativas += 1
    totalTentativas -= 1
    if numEscolhido == numeroSorte:
        print(
            f'o número  escolhido foi {numEscolhido} Parabéns você acertou, o numero da sorte é {numeroSorte}')
        print(f'acertou em {qtdadeTentativas} Tentativas!')
        break
    else:
        print(
            f'{numEscolhido} Infelizmente Não acertou!, o numero da sorte é {numeroSorte}')
        print(
            f'Efetuou {qtdadeTentativas} tentativas, restam {totalTentativas} num total de  3')

    if totalTentativas == 0:
        print("Esgotou o número máximo de tentativas!")
        controlo = False

    numeroSorte = randint(1, 10)

print("O jogo terminou...")
