nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Sergio", "idade": 51}

# 1a. forma: é a mais antiga, quase não utilizada hoje em dia
print("Nome: %s Idade: %d" % (nome, idade))

# 2a. forma: (.format - mas já tem uma mais moderna)
print("Nome: {} Idade: {}".format(nome, idade))
# se colocar os índices, as variáveis dentro do format não 
# precisam necessariamente estarem na ordem; posso repetir a 
# exibição de uma variável tantas vezes quanto eu quiser
print("Nome: {1}, Idade: {0}, olá {1}".format(idade, nome))
# posso passar o nome diretamente:
print("Nome: {nome}, Idade: {age}, olá {nome}".format(age=idade, nome=nome))
# também posso passar as chaves do dicionário:
print("Nome: {nome}, Idade: {idade}, olá {nome}".format(**dados))

# 3a. forma: f string (atual), é mais simplificado
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")
# com a 3a. forma, também consigo formatar os números, no exemplo abaixo
# quero que o número inteiro ocupe 10 casas e a parte decimal 2 casas,
# é arredondado as casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
# se eu quiser formatar o saldo, apenas na parte decimal:
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")