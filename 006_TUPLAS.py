# tuplas - imutável
tupla = ()
tupla = tuple()
tupla = 2, 3, 4, 'texto'
tupla = (2, 5, 6, 9)

print(tupla[1])
print(tupla[0:3])
print(tupla[-1])

for i in tupla:
    print(i)

tuplaOrdenada = sorted(tupla, reverse=True)
print(f"\n{tuplaOrdenada}\n")

print(5 in tupla)
print(tupla.count(2))
print(tupla.index(5))
print(len(tupla))

tupla = tuple(input(f"Digite o {x + 1}º nome: ") for x in range(3))
print(tupla)

# ex. brasileirão - vogais
times = ("Bahia", "Botafogo", "Bragantino", "Ceará", "Corinthians",
"Cruzeiro", "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Internacional",
"Juventude", "Mirassol", "Palmeiras", "Santos", "Sport", "São Paulo", "Vasco",
"Vitória")

vogais = ('a', 'ã', 'á', 'e', 'ê', 'i', 'o', 'ó', 'u')
letras = ''

for time in times:
    for letra in time:
        if letra.lower() in vogais:
            letras = letras + letra
    print(f"{time, letras.lower()}")
    letras = ''