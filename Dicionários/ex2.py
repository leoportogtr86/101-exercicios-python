### 2. **Acessando Valores**

# Dado um dicionário com as seguintes informações: `{"nome": "Maria", "idade": 25, "cidade": "São Paulo"}`,
# acesse e imprima apenas o valor correspondente à chave "cidade".
# Adicione uma nova chave "email" ao dicionário do exercício anterior e atribua um valor a ela.
### 4. **Atualizando Valores**

# Atualize o valor da chave "idade" no dicionário do exercício 2 para 26.
### 5. **Removendo Pares**

# Remova a chave "cidade" do dicionário do exercício 2 usando o método `pop()` e imprima o valor removido.


pessoa = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "São Paulo",
    "email": "maria@bol.com.br"
}


pessoa["idade"] = 26

print(pessoa["cidade"])
pessoa.pop("cidade")

print(pessoa)