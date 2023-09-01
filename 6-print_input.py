nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
print(nome, idade)
print("teste") # a quebra de linha já vem embutida se não colocar nada
print("teste", end=" ")
print(nome, idade, end="...\n")
print(nome, idade, sep="#") # muda o separador de uma variável e outra por #
print(nome, idade, sep="#", end="...\n")