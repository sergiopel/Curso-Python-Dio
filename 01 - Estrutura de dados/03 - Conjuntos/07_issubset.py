conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# compara se o conjunto de a é subconjunto de b
resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

# compara se o conjunto de b é subconjunto de a
resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)
