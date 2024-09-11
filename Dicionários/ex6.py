# ### 6. **Verificando Chaves**
#
# Escreva um código que verifique se a chave "telefone" está presente no dicionário do exercício 2.
pessoa = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "São Paulo",
    "email": "maria@bol.com.br"
}

if "telefone" in pessoa:
    print("A chave está presente no dicionário.")
else:
    print("A chave não está presente no dicionário.")
