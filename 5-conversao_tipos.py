# converter float para int, neste exemplo retorna 1
print(int(1.95))

# converter string para inteiro
print(int("10"))

# converter string para float
print(float("10.12"))

# converter int para float
print(float(100))

# converter número para string
print(str(10.10))

# converter número para string, para comprovar que virou string fazemos o seguinte:
print(type(str(10.10)))

# mais exemplos para verificar o tipo da string:
valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

# divisão retornando float (utiliza-se uma barra de divisão: '/')
print(100 / 2)

# divisão retornando inteiro (utiliza-se duas barras de divisão: '//')
print(100 // 2)

idade = 51
preco = 1000.57
# concatenando
texto = f"Idade {idade} preco {preco}"
print(texto)

