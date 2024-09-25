# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 7.0

def calcular_notas():
    notas = []

    # Coletando as notas dos alunos
    for i in range(5):
        nota = float(input(f"Nota do aluno {i + 1}: "))
        notas.append(nota)

    # Calculando maior, menor e média
    maior_nota = max(notas)
    menor_nota = min(notas)
    media_nota = sum(notas) / len(notas)

    # Exibindo os resultados
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Média das notas: {media_nota:.1f}")

calcular_notas()
