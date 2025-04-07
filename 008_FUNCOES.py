# sintaxe da função:
# def nome(parâmetros opcionais):
#      código
#      return (opcional)
# nome() - chamar função

# função sem parâmetro:
print()
input()

# função com parâmetro:
max([1, 2, 3, 4, 5])
min([1, 2, 3, 4, 5])

# funções importadas do python
import os
import time
time.sleep(1)
os.system('cls')

# função importada que necessita de instalação:
import click
click.clear() # apagar o console

# função criada pelo dev (sem parâmetro):
def ola():
    print('Olá')
ola()

# função criada pelo dev (com parâmetro):
def soma(n1, n2):
    return n1 + n2

print(soma(5, 6))

# ex. função
numero = float(input("\nDigite um número: "))
numero2 = float(input("Digite um número: "))

print(soma(numero, numero2))

# função com nº fatores:
def infinito(*n):
    print(n)
infinito(2, 3, 5, 5, 8, 1000)

print('ola', 'sou', 'mariana', 'tenho', 18, 'anos')

variavel_global = 5 # variável global

def numero():
    # global variavel_global - passa a ser a mesma linha comentada no escopo

    variavel_global = 10 # variável local
    print(variavel_global)

numero()
print(variavel_global)

# ex. fatorial
def fatorial(numero):
    if numero < 0:
        return None
    if numero < 2:
        return 1

    return numero * fatorial(numero - 1)

print(fatorial(5))

# ex. cadastro com dicionários
from random import randint

jogador = {}
lista = []

def cadastro():
    jogador['nome'] = input("Informe o nome: ")

    while True:
        try:
           jogador['qtd_partidas'] = int(input("Informe o número de partidas: "))
        except(ValueError, TypeError): # sozinho: qualquer exceção
            print("Digite apenas números inteiros!!\n")
        except FileNotFoundError():
            print("Arquivo não encontrado <nome do arquivo>.")
        except:
            print("Erro inesperado!")
        else:
            break

    jogador['gols'] = 0
    print()

    for j in range(jogador['qtd_partidas']):
        jogador['gols'] += randint(0, 3)
        jogador['detalhes'] = round(jogador['gols'] / jogador['qtd_partidas'], 2)
        lista.append(jogador.copy())

def consulta():
    nome_jogador = input("De qual jogador você deseja exibir os dados? ")
    print()

    for i in lista:
        if nome_jogador in i['nome']:
            for k, v in i.items():
                print(f"{k}: {v}")
            break
    else:
        print("Jogador não encontrado.\n")

        opcao = input("Deseja cadastrar? (S/N)\n").upper()

        if opcao == 'S':
            cadastro()
        else:
            exit()

while True:
    menu = input('    [1] Cadastro\n    [2] Consulta\n    [3] Sair\n\nEscolha: ')

    match menu:
        case '1':
            cadastro()

        case '2':
            consulta()
        case '3':
            break
        case _:
            print("Opção inválida!")