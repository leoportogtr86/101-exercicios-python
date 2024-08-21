# 11. **Verificar Ano Bissexto**: Determine se um ano é bissexto ou não.
def is_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False


print(f"{2024} - {is_bissexto(2024)}")
print(f"{2025} - {is_bissexto(2025)}")
print(f"{2026} - {is_bissexto(2026)}")
print(f"{2027} - {is_bissexto(2027)}")
print(f"{2028} - {is_bissexto(2028)}")
print(f"{2029} - {is_bissexto(2029)}")
