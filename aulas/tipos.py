algo = input('Digite algo para saber o tipo: ')

print("")
print("Tipo texto: {}".format(algo.isalpha()))
print("Tipo numero: {}".format(algo.isalnum()))
print("Tipo alpha numerico: {}".format(algo.isalnum()))
print("Caixa alta: {}".format(algo.isupper()))
print("Caixa baixa: {}".format(algo.islower()))
print("Espaço vazio: {}".format(algo.isspace()))

# Para saber o tipo de dado da variavel use o type()

print("")
print("")
print("-------------------------------------------")
print("")
print("Para saber o tipo de dado da variavel use o type()")
print("O tipo é: {}".format(type(algo)))
print("")
print("-------------------------------------------")


# Resultado: type('Shin Megami')
#
# Tipo 'texto'
# <class 'str'>

# Resultado: type(42)
#
# Tipo numerico 'Inteiro'
# <class 'float'>

# Resultado: type(7.7)
#
# Tipo numerico 'Real'
# <class 'float'>

# Resultado: type(True)
#
# Tipo 'boleano'
# <class 'bool'
