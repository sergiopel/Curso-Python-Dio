def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# Com argumentos nomeados não se corre o risco de inverter a ordem dos parâtros recebidos
# na função e posso até trocar a ordem dos argumentos nomeados na chamada:
print("=" * 60)
salvar_carro(marca="Fiat", modelo="Palio", placa="ABC-1234", ano=1999)
print("=" * 60)
# neste exemplo, os 2 asteriscos indica que estou passando um dicionário para
# a função salvar_carro
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
