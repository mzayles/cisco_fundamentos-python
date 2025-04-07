# dicionários
aluno = {}
aluno = dict()

aluno = {
    'turma': 'T3C',
    'nome': 'Mariana',
    'idade': 18,
    'altura': 1.62
}

print(aluno['nome'])
print()

aluno['turma'] = '1MC'
print(aluno)
aluno['genero'] = 'feminino'
print(aluno)
print()

for i in aluno:
    print(i)

for i in aluno.values():
    print(i)

print()

for k, v in aluno.items():
    print(f"{k}: {v}")