saldo = 1000
limite = 500

# saldo ocupa a mesma região de memória de limite ?
print(saldo is limite)

# saldo não ocupa a mesma região de memória de limite ?
print(saldo is not limite)

saldo = 1000
limite = 1000
print()

# saldo ocupa a mesma região de memória de limite ?
print(saldo is limite)

# saldo não ocupa a mesma região de memória de limite ?
print(saldo is not limite)
