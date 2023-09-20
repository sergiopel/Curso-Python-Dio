saldo = 0

while True:
  valor = float(input())
  if valor > 0:
    saldo += valor
    print(f"Deposito realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}")
  elif valor == 0:
    print(f"Encerrando o programa...")
    break
  else:
    print(f"Valor invalido! Digite um valor maior que zero.")