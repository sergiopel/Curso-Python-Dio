# método extend adiciona no final da lista o conteúdo de uma outra lista
# se a lista a adicionar tiver algum elemento igual à primeira lista, 
# ficará repetido
# lembrando que o append adiciona de 1 em 1

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp", "c"])

print(linguagens)  # ["python", "js", "c", "java", "csharp", "c"]
