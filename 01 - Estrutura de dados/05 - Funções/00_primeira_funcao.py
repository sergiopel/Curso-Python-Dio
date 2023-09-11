# Função pode receber ARGUMENTOS
def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome_2):
    print(f"Seja bem vindo {nome_2}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
# Quando chamamos a função, podemos passar PARÂMETROS. É opcional colocar o nome da variável que receberá, na função
# mas se eu quisesse eu poderia colocar (nome_2="João")
exibir_mensagem_2("João")
exibir_mensagem_3()
exibir_mensagem_3(nome="Sergio")
