# loop for - ex. tabuada
# range(início, fim, salto)
num = 8

for i in range(0, 11):
    print(f"{num} x {i} = {num * i}")

# for com str
palavra = 'python'

for i in range(len(palavra)):
    print(palavra[i])

# ex. números primos com for
num = int(input("Digite um número: "))

if num < 2:
    print("Não é primo!")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Não é primo!")
            break
    else:
        print("É primo!")