# loop while
x = 10

while x > 0:
    x -= 1 # incremento / decremento

    if x == 5:
        # continue
        break
    print(x)
print("Fim do programa.")

# ex. tabuada simples
x = 0

num = int(input("Digite um número para saber a tabuada: "))
print()

while x <= 10:
    print(f"{x} x {num} = {x * num}")
    x += 1
    break # não terminou de "morte morrida"
else:
    print("\nFim do programa.")

# ex. tabuada completa
x = 0

while x <= 10:
    j = 0
    print()

    while j <= 10:
        print(f"{x} x {j} = {x * j}")
        j += 1

        if x == 5:
            break
    x += 1

while True:
    print('Teste')
    if 5 > 3:
        break

print('Fim!')

# ex. password
from time import sleep

senha = '1234'
tentativa = 3
tempo = 10

while tentativa > 0:
    psw = input("Digite sua senha: ")

    if psw == senha:
        print("Bem vindo(a)!")
        break
    else:
        tentativa -= 1

    if tentativa == 0:
        print(f"\nIndisponível. Tente novamente em {tempo} segundos.\n")
        sleep(tempo)
        tempo += 10
        tentativa = 3