# O python nos permite retornar mais de um valor, caso seja necessário
# Se não tiver o return no final da função, preciso colocar um print e chamar a função
# sem o print antes
# Se tiver o return no final da função, preciso chamar a função com print antes e o
# retorno será uma tupla
def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

# neste caso vai retornar 2 valores em uma tupla    
    return antecessor, sucessor


def teste(num1=1, num2=2):
    print(f"Números {num1} e {num2}")

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
teste()