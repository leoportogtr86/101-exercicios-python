# Usando Lambdas em Python: Um Guia Completo

## Introdução

Em Python, as funções lambda são conhecidas como funções anônimas ou funções pequenas, uma vez que não precisam de um
nome explícito e geralmente são definidas em uma única linha. Elas são úteis quando precisamos de uma função para ser
usada temporariamente, em um curto espaço de código, especialmente quando essa função não será reutilizada
posteriormente. Este artigo abordará o que são funções lambda, quando e como utilizá-las, além de alguns exemplos
práticos para ilustrar seu uso.

## O que é uma Função Lambda?

Uma função lambda em Python é uma função pequena e anônima que pode ter qualquer número de argumentos, mas apenas uma
expressão. A expressão é avaliada e retornada. O uso da palavra-chave `lambda` indica a criação de uma função lambda. A
sintaxe básica é:

```python
lambda argumentos: expressão
```

### Exemplo Básico

Aqui está um exemplo simples de uma função lambda que soma dois números:

```python
soma = lambda a, b: a + b
resultado = soma(2, 3)
print(resultado)  # Saída: 5
```

Neste exemplo, a função lambda recebe dois argumentos (`a` e `b`) e retorna a soma deles.

## Quando Usar Funções Lambda?

As funções lambda são úteis em várias situações, especialmente quando precisamos passar uma função como argumento para
outra função. Elas são frequentemente usadas com funções como `map()`, `filter()` e `sorted()`, onde uma função simples
é necessária como argumento.

### Usando com `map()`

A função `map()` aplica uma função a todos os itens em um iterável (como uma lista) e retorna um mapa (que pode ser
convertido em uma lista ou outro tipo de coleção).

```python
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
```

Neste exemplo, uma função lambda é usada para calcular o quadrado de cada número na lista.

### Usando com `filter()`

A função `filter()` filtra os itens de um iterável, retornando aqueles para os quais a função fornecida retorna `True`.

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6]
```

Aqui, a função lambda filtra os números pares da lista.

### Usando com `sorted()`

A função `sorted()` pode aceitar uma função chave para determinar a ordem de classificação. Lambdas são frequentemente
usadas para definir essa chave.

```python
pessoas = [('João', 30), ('Ana', 25), ('Pedro', 40)]
ordenado_por_idade = sorted(pessoas, key=lambda x: x[1])
print(ordenado_por_idade)  # Saída: [('Ana', 25), ('João', 30), ('Pedro', 40)]
```

Neste exemplo, a função lambda classifica a lista de tuplas pelo segundo item de cada tupla (a idade).

## Limitações das Funções Lambda

Embora as lambdas sejam úteis em muitos casos, elas têm algumas limitações:

1. **Apenas uma expressão**: As funções lambda podem conter apenas uma única expressão, o que significa que não podem
   realizar múltiplas operações ou declarações complexas.
2. **Código menos legível**: Em alguns casos, o uso excessivo de lambdas pode tornar o código mais difícil de entender,
   especialmente para funções mais complexas.

## Conclusão

Funções lambda em Python são uma ferramenta poderosa e conveniente para situações onde uma função simples é necessária
por um curto período de tempo. Elas são frequentemente usadas em conjunto com funções como `map()`, `filter()`
e `sorted()`, permitindo escrever código mais conciso e direto. No entanto, é importante usá-las de forma adequada, pois
podem sacrificar a legibilidade se não forem usadas corretamente.

Compreender como e quando usar lambdas pode aumentar a eficiência do seu código, especialmente em cenários onde você
precisa de funções pequenas e rápidas.