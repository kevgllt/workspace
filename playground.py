# Caixa hortifruti Bahia`S

#fr = Fruta

fr_0 = 'Laranja'
fr_1 = 'Morango'
fr_2 = 'Melão  '
fr_3 = 'Banana '
fr_4 = 'Uva    '
fr_5 = 'Manga  '
#qt = Quantidade
qt_0 = 200
qt_1 = 100
qt_2 = 40
qt_3 = 200
qt_4 = 100
qt_5 = 75
#Pr = Preço
pr_0 = 50
pr_1 = 35
pr_2 = 12
pr_3 = 20
pr_4 = 18
pr_5 = 22

print("------------------Bahia`S--------------------")
print("")
print("="*18,"Estoque","="*18)
print("")
print("|item|"," "*5,"|QUANTIDADE|"," "*5,"|PREÇO|")
print("")
print("{:8}{:12}{:16}".format(fr_0, qt_0, pr_0))
print("{:8}{:12}{:16}".format(fr_1, qt_1, pr_1))
print("{:8}{:12}{:16}".format(fr_3, qt_3, pr_3))
print("{:8}{:12}{:16}".format(fr_2, qt_2, pr_2))
print("{:8}{:12}{:16}".format(fr_4, qt_4, pr_4))
print("{:8}{:12}{:16}".format(fr_5, qt_5, pr_5))
print("")
print("")
print('-'*50)


# Posicionamento 

# lado esquerdo
# print("Ola {:=<20} !")

# lado direto
# print("Ola {:=>20} !")

# lado centralizado
#print("Ola {:=^20} !")
