# O conjunto pode ser definido com o set, ou usando chaves
# o set retira elementos repetidos e não garante a ordem no print
# não é possível acessar índices de um conjunto, mas se precisar consumir
# esses elementos, será preciso converter o set em uma lista
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)


