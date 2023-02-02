# 1- Utilizando o laco IF verifica se uma pessoa é maior ou menor

idade = int(input("Introduz a idade da pessoa: "))
if idade >= 18:
    print(f'Maior de idade: {idade} anos')
else:
    print(f'Menor de idade: {idade} anos')

# 2- Utilizando o laco elif para verificar muitas condicoes
# Controlo de velocidade de um veiculo

velocidade = int(input("Qual é a velocidade? "))
if velocidade < 40:
    print("Velocidade baixa!")
elif velocidade < 100:
    print("Velocidade moderada!")
else:
    print("Tenha cuidado, modere a velocidade!")

# 3- Controlo de fluxo utilizando o laco FOR

nomes = ['Ana', 'Bruno', 'JOSE', 'MARIA', 'ZECA']
\
cont = 0
for nome in nomes:
    cont = cont + 1
    # o lower é para transformar os nomes em minúscula
    print("{}- {}" .format(cont, nome.lower()))

# 4- Utilizando a funcao ZIP para empacotar duas listas e o FOR para percorrer e mostrar a a mesma

nomes = ['pedro', 'joao', 'Miguel']
idades = [28, 55, 30]

lista_tuplas = zip(nomes, idades)
for nome, idade in lista_tuplas:
    print("{} tem {} anos ".format(nome, idade))

for indice, idad in enumerate(idades):
    if idad > 50:
        print(f"indice {indice} Maior do que 50 ")
