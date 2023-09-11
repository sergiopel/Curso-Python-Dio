# antes do "/", só posso passar parâmetros na chamada da função SOMENTE por posição,
# mas depois da "/" eu posso passar os parâmetros nomeados ou não, tanto faz
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# funciona:
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# funciona:
criar_carro("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina")
# dá erro:
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
