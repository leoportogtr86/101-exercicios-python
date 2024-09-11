# ### 9. **Percorrendo Pares Chave-Valor**
#
# Percorra o dicionário do exercício 1 usando o método `items()` e imprima os pares chave-valor.
produto = {
    "nome": "Laptop",
    "preco": 7800,
    "quantidade": 10
}

for key, value in produto.items():
    print(f"Chave: {key}. Valor: {value}")
