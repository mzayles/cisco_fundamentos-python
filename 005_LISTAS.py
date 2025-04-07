"""
    exc = bancos.pop()
    pop() - padrão -1
    len(bancos[1])
    bancos.sort(reverse=True)
"""

# listas
bancos = ['caixa', 'nubank', 'nubank', 'itaú', 'banco do brasil', 'safra', 'caixa', 'c6', 'itaú', 'itaú']
print(bancos)
print(bancos[0:10:2]) # pulo de 2 em 2

# altera uma, altera a outra
lista = bancos.copy() # bancos[:]
print(lista)

lista.remove('nubank')

print(bancos)
print(lista)

# endereço
print(id(lista))
print(id(bancos))

# percorrer lista
for i in range(len(bancos)):
    print(bancos[i])

for i in bancos:
    print(i)

# contar dentro de uma lista
soma = 0

for banco in bancos:
    soma += banco.count('a')
print(soma)

# listas com loop for
lista = [1, 2, 3, 4, 5, 6, 7]

for i in range(3):
    lista.insert(lista[3], i)
print(lista)

lista = [i for i in range(3)]
print(lista)

lista = [[j for j in range(3)] for i in range(3)]
for i in lista:
    print(i)

# tabuleiro de xadrez
lista = [['' for j in range(8)] for i in range(8)]
lista[7][0] = lista[7][7] = lista[0][0] = lista[0][7] = 'T'

linha = int(input("Escolha a linha: "))
coluna = int(input("Escolha a coluna: "))

lista[linha][coluna] = 'X'

# exibir lista
for i in lista:
    print(i)

# ordenação manual
lista = [1, 0, 9, 2, 22, 7]

for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            print(lista)

# ex. brasileirão
times = ["Bahia", "Botafogo", "Bragantino", "Ceará", "Corinthians",
"Cruzeiro", "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Internacional",
"Juventude", "Mirassol", "Palmeiras", "Santos", "Sport", "São Paulo", "Vasco",
"Vitória"]

# 5 primeiros colocados
primeiros5 = times[:5]
print(f"Os 5 primeiros colocados são: ", end='')
for i in primeiros5:
    print(i, end=', ')

# 5 últimos colocados
ultimos4 = times[-4:]
print(f"\n\nOs 4 primeiros colocados são: ", end='')
for i in ultimos4:
    print(i, end=', ')

# ordem alfabética
print(f"\n\nLista em ordem alfabética:")
for i in times:
    print(i, end=', ')

# posição do Mirassol
print(f"\n\nO Mirassol está na posição {times.index('Mirassol')}.")