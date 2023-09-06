# método remove é a segunda forma de retirar elementos de uma lista
# a diferença é que é passado o objeto diretamente
# lembrando que se tiver mais de uma ocorrencia de um elemento, será
# removido apenas a primeira ocorrencia, mas para remover todas
# precisaria fazer uma lógica com o count para remover todas as 
# ocorrências

linguagens = ["python", "js", "c", "java", "csharp", "c"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]
