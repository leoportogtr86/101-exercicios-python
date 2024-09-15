# Lista de 20 Exercícios Sobre Funções em Python

Abaixo estão 20 exercícios projetados para ajudá-lo a praticar e aprofundar seu conhecimento sobre funções em Python. Os
exercícios variam em dificuldade e cobrem diferentes aspectos do uso de funções.

---

## 1. Função de Saudação Simples

**Descrição:** Escreva uma função chamada `saudar()` que exiba a mensagem "Olá, Mundo!" quando chamada.

```python
def saudar():
# Seu código aqui
```

---

## 2. Função com Parâmetro

**Descrição:** Crie uma função chamada `exibir_nome(nome)` que receba um nome como parâmetro e exiba "Olá, [nome]!".

```python
def exibir_nome(nome):
# Seu código aqui
```

---

## 3. Função com Retorno

**Descrição:** Escreva uma função `soma(a, b)` que receba dois números e retorne a soma deles.

```python
def soma(a, b):
# Seu código aqui
```

---

## 4. Parâmetros Padrão

**Descrição:** Crie uma função `potencia(base, expoente=2)` que retorne a base elevada ao expoente. Se o expoente não
for fornecido, use 2 como padrão.

```python
def potencia(base, expoente=2):
# Seu código aqui
```

---

## 5. Função que Verifica Número Primo

**Descrição:** Escreva uma função `eh_primo(n)` que verifique se um número inteiro positivo `n` é primo. A função deve
retornar `True` se for primo e `False` caso contrário.

```python
def eh_primo(n):
# Seu código aqui
```

---

## 6. Função com *args

**Descrição:** Crie uma função `media(*numeros)` que receba uma quantidade variável de números e retorne a média
aritmética deles.

```python
def media(*numeros):
# Seu código aqui
```

---

## 7. Função com **kwargs

**Descrição:** Escreva uma função `informacoes_pessoais(**kwargs)` que receba dados pessoais como argumentos nomeados e
exiba as informações no formato "chave: valor".

```python
def informacoes_pessoais(**kwargs):
# Seu código aqui
```

---

## 8. Calculadora Simples

**Descrição:** Crie uma função `calculadora(a, b, operacao)` que receba dois números e uma operação (`'soma'`,
`'subtracao'`, `'multiplicacao'`, `'divisao'`) e retorne o resultado da operação.

```python
def calculadora(a, b, operacao):
# Seu código aqui
```

---

## 9. Recursão - Fatorial

**Descrição:** Escreva uma função recursiva `fatorial(n)` que calcule o fatorial de um número inteiro positivo `n`.

```python
def fatorial(n):
# Seu código aqui
```

---

## 10. Função Lambda

**Descrição:** Use uma função lambda para criar uma função que retorne o dobro de um número fornecido.

```python
dobro =  # Seu código aqui
```

---

## 11. Map e Lambda

**Descrição:** Dada a lista `numeros = [1, 2, 3, 4, 5]`, use a função `map()` e uma função lambda para obter uma nova
lista com os números elevados ao quadrado.

```python
numeros = [1, 2, 3, 4, 5]
quadrados =  # Seu código aqui
```

---

## 12. Filter e Função

**Descrição:** Escreva uma função `eh_par(n)` que verifique se um número é par. Use essa função com `filter()` para
obter apenas os números pares da lista `numeros = [1, 2, 3, 4, 5, 6]`.

```python
def eh_par(n):


# Seu código aqui

numeros = [1, 2, 3, 4, 5, 6]
pares =  # Seu código aqui
```

---

## 13. Função que Modifica Variável Global

**Descrição:** Declare uma variável global `contador = 0`. Crie uma função `incrementar()` que incremente o valor de
`contador` em 1 cada vez que for chamada.

```python
contador = 0


def incrementar():
# Seu código aqui
```

---

## 14. Docstrings

**Descrição:** Escreva uma função `converter_temperatura(celsius)` que converta uma temperatura de Celsius para
Fahrenheit. Adicione uma docstring que explique o que a função faz, seus parâmetros e o valor de retorno.

```python
def converter_temperatura(celsius):
    """
    Sua docstring aqui
    """
    # Seu código aqui
```

---

## 15. Função que Retorna Outra Função

**Descrição:** Crie uma função `multiplicador(n)` que retorne uma função lambda que multiplique um número pelo valor de
`n`.

```python
def multiplicador(n):


# Seu código aqui

duplicar = multiplicador(2)
print(duplicar(5))  # Saída esperada: 10
```

---

## 16. Decorador Simples

**Descrição:** Escreva um decorador `tempo_execucao(func)` que calcule o tempo de execução de uma função passada como
argumento.

```python
import time


def tempo_execucao(func):


# Seu código aqui

@tempo_execucao
def soma(a, b):
    return a + b
```

---

## 17. Anotações de Tipo

**Descrição:** Reescreva a função `soma(a, b)` do exercício 3, adicionando anotações de tipo que indiquem que os
parâmetros e o retorno são inteiros.

```python
def soma(a: int, b: int) -> int:
# Seu código aqui
```

---

## 18. Função Geradora

**Descrição:** Crie uma função geradora `gerador_pares(n)` que gere todos os números pares de 0 até `n`.

```python
def gerador_pares(n):


# Seu código aqui

for numero in gerador_pares(10):
    print(numero)
```

---

## 19. Função que Lê Arquivo

**Descrição:** Escreva uma função `ler_arquivo(nome_arquivo)` que leia um arquivo de texto e retorne seu conteúdo.
Adicione tratamento de exceções para lidar com erros de arquivo não encontrado.

```python
def ler_arquivo(nome_arquivo):
# Seu código aqui
```

---

## 20. Função com Documentação Completa

**Descrição:** Escreva uma função `calcular_desvio_padrao(lista)` que calcule o desvio padrão de uma lista de números.
Inclua uma docstring detalhada e anotações de tipo.

```python
def calcular_desvio_padrao(lista: list) -> float:
    """
    Calcula o desvio padrão de uma lista de números.

    :param lista: Lista de números (int ou float).
    :return: O desvio padrão dos números na lista.
    """
    # Seu código aqui
```

---

**Instruções Gerais:**

- Para cada exercício, substitua `# Seu código aqui` pelo código necessário para cumprir a tarefa.
- Teste suas funções para garantir que elas funcionem conforme o esperado.
- Sinta-se à vontade para adicionar tratamentos de erros e casos especiais para tornar suas funções mais robustas.
- Utilize boas práticas de programação, como nomes de variáveis claros e comentários quando necessário.