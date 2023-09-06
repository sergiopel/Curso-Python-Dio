# método pop, se for utilizado vazio, retira o último elemento
# que foi adicionado na lista (pilha)
# se for usado com índice, retira na lista exatamente o elemento do índice
# especificado

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # retira csharp
print(linguagens.pop())  # retira java
print(linguagens.pop())  # retira c
print(linguagens.pop(0))  # retira python

print(linguagens) # só terá o elemento js
