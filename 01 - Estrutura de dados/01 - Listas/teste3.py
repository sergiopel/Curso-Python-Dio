valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

def calcula_juros(valor_inicial, taxa_juros, periodo):
  valor_final = valor_inicial
  for _ in range(periodo):  
    valor_final *= (1 + taxa_juros)
  return valor_final

valor_final = calcula_juros(valor_inicial, taxa_juros, periodo)

print(f"Valor final do investimento: R$ {valor_final:.2f}")

