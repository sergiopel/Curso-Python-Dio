nome = "sERgiO pELEGrini"

# converte a string para maiúsculo
print(nome.upper())
# converte a string para minúsculo
print(nome.lower())
# converte a primeira letra de cada palavra da string para maiúsculo
#  e o restante, para minúsculo
print(nome.title())


texto = "  Olá mundo!     "
print(texto + ".")
# eliminar todos os espaços em branco
print(texto.strip() + ".")
# eliminar espaços à direta
print(texto.rstrip() + ".")
# eliminar espaços à esquerda
print(texto.lstrip() + ".")

# junções e centralização
menu = "Python"
print("####" + menu + "####")
# a instrução acima pode ser substituí por:
print(menu.center(14, "#"))

# colocando um traço entre as letras da string:
print("-".join(menu))

# se fosse fazer com for, teria mais código, assim:
for letra in menu:
    print(letra, end="-")
print()