# ## 4. Parâmetros Padrão
# **Descrição:** Crie uma função `potencia(base, expoente=2)` que retorne a
# base elevada ao expoente. Se o expoente não for fornecido, use 2 como padrão.
import math


def potencia(base, expoente=2):
    return math.pow(base, expoente)


print(potencia(10, 3))
print(potencia(10))
