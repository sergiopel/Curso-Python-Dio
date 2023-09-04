# break e continue podem ser utilizados dentro do while e do for

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break # interrompe o laço

    print(numero)



for numero in range(100):
    if numero == 12:
        continue # não executa o que está embaixo e vai pro próximo laço

    print(numero, end= " ")