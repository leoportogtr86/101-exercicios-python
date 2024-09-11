# ### 10. **Contagem de Ocorrências**
#
# Escreva um programa que conte quantas vezes cada palavra aparece em uma lista de palavras e
# armazene o resultado em um dicionário.

palavras = ["gato", "cachorro", "gato", "gato", "cachorro", "papagaio", "cachorro", "papagaio", "gato"]

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)