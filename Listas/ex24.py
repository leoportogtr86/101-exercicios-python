# 24. **Concatenar Listas**: Concatene duas listas fornecidas pelo usuário.
lista1 = []
lista2 = []
qtd_lista_1 = int(input("Quantos itens deseja inserir na lista 1? "))
qtd_lista_2 = int(input("Quantos itens deseja inserir na lista 2? "))

for i in range(qtd_lista_1):
    item = input("Insira um item a lista 1: ")
    lista1.append(item)

for i in range(qtd_lista_2):
    item = input("Insira um item a lista 2: ")
    lista2.append(item)

lista3 = lista1 + lista2

print(f"Listas concatenadas: {lista3}")
