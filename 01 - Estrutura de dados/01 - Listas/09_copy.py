# efetuar a cópia de uma lista

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
print(l2)     # [1, "Python", [40, 30, 20]]

# pra se certificar que copiou mesmo, podemos utilizar o id:
print(id(lista), id(l2))