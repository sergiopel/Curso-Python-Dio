# Se acessar uma chave do dicionário com o método get, se a chave não 
# existir, não gera exceção, retorna None e continua a execução.
# Mas se acessar a chave do dicionário diretamente assim:
# contatos["chave"] e a chave não existir, interrompe o programa,
# gerando uma exceção.
# Com o get, também podemos retornar um dicionário vazio, caso não
# encontre a chave.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
