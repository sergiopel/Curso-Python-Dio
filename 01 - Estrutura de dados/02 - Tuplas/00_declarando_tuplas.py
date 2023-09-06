# As tuplas são imutáveis, muito parecida com listas, mas não é possível
# alterar os valores dela
# São usados parênteses, que diferencia da lista, que usa colchetes


frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

# posso declarar uma tupla usando o tuple também
letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
