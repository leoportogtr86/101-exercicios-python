# 8. **Calcular Média de Notas**: Receba cinco notas e calcule a média.
notas = []
soma = 0

for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

for i in range(5):
    soma += notas[i]

media = soma / 5

print(f"Média: {media}")
