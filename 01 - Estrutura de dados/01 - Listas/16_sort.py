# método sort, ordena a lista

# se for usado sem argumentos, ordena em ordem alfabética
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# se usar o argumento reverse=True, ordena a lista de trás pra frente,
# funcionando da mesma forma que o método reverse
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# nesse exemplo eu consigo ordenar os elementos da lista
# por ordem de tamanho de caracteres
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

# faz a mesma coisa que o exemplo anterior e no final ordena ao contrário
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)
