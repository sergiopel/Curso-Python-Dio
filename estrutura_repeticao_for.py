texto = input("Informe um texto: ")
VOGAIS = "AÁEÉIÍOÓUÚ"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
# também tem else no for, mas não é muito comum o seu uso
# é mais comum usar o else no if
else:
    print()
    print("Executa no final do laço")

# Exemplo utilizando a função bulti-in 'range'
for numero in range(0, 51, 5):
    print(numero, end=" ")    