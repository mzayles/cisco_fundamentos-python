"""
DOCUMENTAÇÃO PYTHON - CISCO NETWORKING ACADEMY

    MÓDULO 001: introdução à programação de computadores e Python;
    MÓDULO 002: tipos de dados, operadores e operações de 0/1;
    MÓDULO 003: balores booleanos, condicionais, loops, listas, operações lógicas e bit a bit;
    MÓDULO 004: funções, tuplas, dicionários, execuções e processamento de dados.
"""

# introdução - exercício básico
nome = (input("Digite o seu nome: \n"))
idade = int(input(f"{nome}, digite a sua idade: \n"))
altura = float(input(f"{nome}, digite a sua altura: \n"))
peso = float(input(f"{nome}, digite o seu peso: \n"))

print("\n✅Seu nome é", nome, ", a sua idade é", idade, "e a sua altura é", altura)
print(f"💡 O seu IMC é: {peso / altura ** 2:.2f}")

# 20.12E10 - representação de notação científica

# operadores lógicos
nome = 'Mariana'
psw = '123'

print((nome == 'mariana' or nome == 'MARIANA') and psw == '123')