# condicionais - ex. média
media = 5.1

if media > 6:
    print('Aprovado!')
elif media < 6 and media > 5:
    print('Recuperação')
else:
    print('Reprovado!')

print('Fim do programa')

# condicionais - ex. futebol
time1 = input("Informe a quantidade de gols do time 1: ")

if time1.isnumeric():
    time1 = int(time1)
else:
    print('Valor inválido.\n')

time2 = input("Informe a quantidade de gols do time 2: ")
if time2.isnumeric():
    time2 = int(time2)
else:
    print('Valor inválido.')

if type(time1) == int and type(time2) == int:
    if time1 > time2:
        print("\nTime 1 ganhou!")
    elif time2 > time1:
        print("\nTime 2 ganhou!")
    else:
        print("\nJogo empatado!")

# ex. números
numero = int(input("Digite um número: "))

if numero > 0:
    print(f"{numero} é positivo.")
elif numero < 0:
    print(f"{numero} é negativo.")
else:
    print(f"{numero} é neutro.")

# operadores lógicos - ex. triângulo
# and, or e not
lado1 = float(input("Digite o 1º lado: "))
lado2 = float(input("Digite o 2º lado: "))
lado3 = float(input("Digite o 3º lado: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print("\nÉ um triângulo válido!")
else:
    print("\nNão é um triângulo válido.")

# operador ternário
print("\nÉ um triângulo válido!" if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1 else "\nNão é um triângulo válido.")

# ex. ímpar ou par
num = 6

if num  % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# operador ternário
num = 6
print("O número é par." if num % 2 == 0 else "O número é ímpar.")