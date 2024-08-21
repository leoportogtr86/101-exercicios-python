# 9. **Cálculo de Fatorial**: Calcule o fatorial de um número dado.
def caclula_fatorial(numero):
    return 1 if numero == 0 else numero * caclula_fatorial(numero - 1)


print(caclula_fatorial(5))
