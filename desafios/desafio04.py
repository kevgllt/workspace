# 1; Faça um programa que leia algo pelo teclado
#  2; mostre na tela o seu tipo primitivo 
#  e todas as informações possiveis sobre ele.

algo = input("Digite algo: ")

verifica_texto = algo.isalpha()
verifica_numerico = algo.isnumeric()
verifica_letraMai = algo.isupper()
verifica_letraMin = algo.islower()
verifica_textoNum = algo.isalnum()
verifica_espaco = algo.isspace()

print("Seu dado é tipo texto: {}".format(verifica_texto))
print("Seu dado é tipo numerico: {}".format(verifica_numerico))
print("Seu dado esta em letra maiuscula: {}".format(verifica_letraMai))
print("Seu dado esta em letra minuscula: {}".format(verifica_letraMin))
print("Seu dado é tipo Alpha ou numerico: {}".format(verifica_textoNum))
print("Seu dado contem espaço: {}".format(verifica_espaco))