# Strings triplas ou strings múltiplas
# É utilizado a f string com 3 aspas simples ou duplas
# e serve para colocar um texto, cuja conteúdo é preservado
# com todos os espaços antes e depois ao usar o print

nome = "Sergio"

mensagem = f"""
   Olá, meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)

# outro exemplo, observe que quando o texto é impresso diretamente
# nao precisa usar o 'f' do f string
print("""
      **************** MENU **************
      
      1 - Depositar
      2 - Sacar
      0 - Sair

      ************************************

          Obrigado por usar nosso sistema !!!
"""
)