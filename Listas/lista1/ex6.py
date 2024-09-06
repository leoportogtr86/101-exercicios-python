#
# ### **Exercício 6: List Comprehension**
#
# Usando list comprehension, crie uma lista chamada `quadrados` que contenha
# os quadrados dos números de 1 a 10. Imprima a
# lista.

quadrados = [x ** 2 for x in range(1, 11)]

print(quadrados)
