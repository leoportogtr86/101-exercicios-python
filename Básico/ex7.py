# 7. **Jogo da Adivinhação**: Crie um jogo onde o usuário deve adivinhar um
# número aleatório entre 1 e 10.
import random

numero_aleatorio = random.randint(1, 10)

while True:
    numero_usuario = int(input("Digite um número entre 1 e 10: "))
    if numero_usuario > numero_aleatorio:
        print("Oops, tente um número menor")
    elif numero_aleatorio < numero_usuario:
        print("Oops, tente um número maior")
    else:
        print("Parabéns, você acertou!")
        break
