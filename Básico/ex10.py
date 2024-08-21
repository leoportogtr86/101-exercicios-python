# 10. **Sequência de Fibonacci**: Gere a sequência de Fibonacci até o n-ésimo termo.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()


print(fibonacci(10))
