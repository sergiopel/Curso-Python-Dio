# data_extenso, recebe a primeira linha (1o. argumento)
# *args e **kwargs (poderia ser qquer nome, o que manda são os * e **)
# Com um asterisco, os valores virão como uma tupla (valores separados por vírgula)
# então *args recebe todos os argumentos separados por vírgula (2a. linha em diante) e
# finaliza antes de começar o argumento com chave e valor
# Com 2 asteriscos, os valores virão como um dicionário (chave e valor)
# pegando então os 2 últimos argumentos recebidos
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args) # concatenando todos os valores recebidos com \n,
                            # ou seja, vai ficar um em cada linha
    # recebe kwargs.items() como uma lista de tuplas com chave e valor (.items), em seguida
    # vai iterar a lista de tuplas (for chave, valor in kwargs.items()) e no fim cria uma
    # string onde é colocado chave e valor e concatenando com \n, vai ficar um meta dado
    # por linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Sábado, 09 de Setembro de 2023",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)
