# método do set (difference), lista os elementos que estão em a,
# mas não estão em b, ou os que estão em b e não estão em a

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)
