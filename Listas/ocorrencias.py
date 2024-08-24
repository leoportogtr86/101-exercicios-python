lista = [10, 20, 10, 20, 30, 45, 4, 45, 100, 100]
contagem = {}

for i in lista:
    if i in contagem:
        contagem[i] += 1
    else:
        contagem[i] = 1

print(contagem)
