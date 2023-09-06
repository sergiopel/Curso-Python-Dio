# função sorted, ordena iteráveis, tem o mesmo resultado 
# do método sort

linguagens = ["python", "js", "c", "java", "csharp"]

# ordenar em ordem de tamanho em caracteres dos elementos
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
# ordenar em ordem de tamanho em caracteres dos elementos, mas no final inverte
# ao contrário
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

# se for ordenar em ordem alfabética:
print(sorted(linguagens))