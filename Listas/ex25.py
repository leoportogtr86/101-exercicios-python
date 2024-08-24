# 25. **Contar Ocorrências**: Conte quantas vezes um determinado valor aparece em uma lista.
lista = ["bola", "boneca", "video game", "video game", "bola de gude", "bola de gude", "boneca", 10, 12, 10]
contagem = {}

for i in lista:
    if i in contagem:
        contagem[i] += 1
    else:
        contagem[i] = 1

print(contagem)
