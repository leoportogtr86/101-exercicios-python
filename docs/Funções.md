# Tudo o Que Você Precisa Saber Sobre Funções em Python

As funções são blocos fundamentais na programação que permitem organizar o código de forma modular, reutilizável e
legível. Em Python, as funções são cidadãos de primeira classe, o que significa que podem ser atribuídas a variáveis,
passadas como argumentos e retornadas por outras funções. Neste artigo, exploraremos em detalhes tudo o que você precisa
saber sobre funções em Python.

## O Que São Funções?

Uma função é um bloco de código nomeado que realiza uma tarefa específica. Ela pode receber entradas (parâmetros) e pode
retornar um valor. As funções ajudam a dividir programas complexos em partes menores e mais gerenciáveis.

## Por Que Usar Funções?

- **Reutilização de Código**: Escreva uma vez, use múltiplas vezes.
- **Organização**: Torna o código mais limpo e estruturado.
- **Manutenção**: Facilita a atualização e correção de erros.
- **Legibilidade**: Ajuda outros programadores a entender o código.

## Definindo Funções

Em Python, as funções são definidas usando a palavra-chave `def`, seguida pelo nome da função e parênteses contendo os
parâmetros.

```python
def nome_da_funcao(parâmetros):
    """Docstring opcional."""
    corpo_da_funcao
    return valor_retorno
```

**Exemplo:**

```python
def saudacao(nome):
    """Exibe uma saudação personalizada."""
    print(f"Olá, {nome}!")
```

## Chamando Funções

Para executar uma função, basta chamá-la pelo nome e passar os argumentos necessários.

```python
saudacao("Alice")  # Saída: Olá, Alice!
```

## Parâmetros e Argumentos

- **Parâmetros**: Variáveis listadas na definição da função.
- **Argumentos**: Valores passados para a função quando ela é chamada.

### Tipos de Parâmetros

1. **Parâmetros Posicionais**: Recebem argumentos na ordem em que são definidos.
2. **Parâmetros Nomeados (Keyword Arguments)**: Argumentos passados com o nome do parâmetro.

**Exemplo:**

```python
def exibir_informacoes(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")


exibir_informacoes("Bob", 30)
exibir_informacoes(idade=25, nome="Carol")
```

## Valores Padrão de Parâmetros

Você pode definir valores padrão para parâmetros, tornando-os opcionais ao chamar a função.

```python
def conectar(host="localhost", porta=8080):
    print(f"Conectando a {host} na porta {porta}")


conectar()  # Usa valores padrão
conectar(porta=9090)  # Sobrescreve o valor padrão da porta
```

## Argumentos Variáveis

### *args (Argumentos Posicionais Variáveis)

Permite que a função receba um número variável de argumentos posicionais.

```python
def soma(*numeros):
    resultado = sum(numeros)
    return resultado


print(soma(1, 2, 3))  # Saída: 6
```

### **kwargs (Argumentos Nomeados Variáveis)

Permite que a função receba um número variável de argumentos nomeados.

```python
def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


exibir_dados(nome="Diana", idade=28, cidade="Rio de Janeiro")
```

## Valor de Retorno

As funções podem retornar valores usando a palavra-chave `return`. Se `return` não for especificado, a função retorna
`None` por padrão.

```python
def multiplicar(a, b):
    return a * b


resultado = multiplicar(5, 4)  # resultado = 20
```

## Funções Lambda (Funções Anônimas)

São funções pequenas e anônimas definidas com a palavra-chave `lambda`.

```python
quadrado = lambda x: x ** 2
print(quadrado(5))  # Saída: 25
```

São frequentemente usadas em conjunto com funções como `map()`, `filter()` e `sorted()`.

## Escopo de Variáveis

- **Escopo Local**: Variáveis definidas dentro da função.
- **Escopo Global**: Variáveis definidas no corpo principal do script.

```python
x = 10  # Variável global


def func():
    x = 5  # Variável local
    print(x)


func()  # Saída: 5
print(x)  # Saída: 10
```

Para modificar uma variável global dentro de uma função, use a palavra-chave `global`.

```python
def alterar_global():
    global x
    x = 20


alterar_global()
print(x)  # Saída: 20
```

## Recursão

Uma função que chama a si mesma. Deve ter uma condição de parada para evitar loops infinitos.

**Exemplo: Fatorial Recursivo**

```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(5))  # Saída: 120
```

## Funções de Ordem Superior

Funções que podem receber outras funções como argumentos ou retornar funções.

**Exemplo:**

```python
def aplicar_operacao(x, operacao):
    return operacao(x)


resultado = aplicar_operacao(5, lambda x: x ** 2)
print(resultado)  # Saída: 25
```

## Decoradores

São funções que recebem outra função como argumento e estendem seu comportamento sem modificá-la explicitamente.

**Exemplo:**

```python
def decorador(func):
    def wrapper():
        print("Antes da função.")
        func()
        print("Depois da função.")

    return wrapper


@decorador
def funcao_principal():
    print("Função principal executada.")


funcao_principal()
```

**Saída:**

```
Antes da função.
Função principal executada.
Depois da função.
```

## Anotações de Funções (Type Hints)

Permitem adicionar informações sobre os tipos esperados de parâmetros e retornos.

```python
def soma(a: int, b: int) -> int:
    return a + b
```

As anotações não afetam a execução, mas são úteis para ferramentas de análise estática e para melhorar a legibilidade.

## Docstrings

Strings de documentação que descrevem o propósito e o uso da função. Devem ser escritas logo após a definição da função.

```python
def dividir(a, b):
    """
    Divide 'a' por 'b' e retorna o resultado.

    :param a: Dividendo.
    :param b: Divisor.
    :return: Quociente da divisão.
    """
    return a / b
```

## Funções Embutidas

Python fornece várias funções embutidas úteis, como `print()`, `len()`, `type()`, `range()`, entre outras.

**Exemplo:**

```python
lista = [1, 2, 3, 4]
print(len(lista))  # Saída: 4
```

## Boas Práticas

- **Nomes Significativos**: Use nomes que descrevam a função.
- **Coesão**: Cada função deve realizar uma única tarefa.
- **Modularização**: Divida o código em funções menores quando possível.
- **Documentação**: Sempre documente suas funções com docstrings.
- **Tratamento de Erros**: Considere adicionar verificações e exceções para entradas inválidas.

## Conclusão

Funções são elementos essenciais em Python que permitem escrever código eficiente, organizado e reutilizável.
Compreender como definir, chamar e manipular funções é fundamental para qualquer programador que deseja dominar a
linguagem. Esperamos que este artigo tenha esclarecido os conceitos e técnicas importantes relacionados às funções em
Python.