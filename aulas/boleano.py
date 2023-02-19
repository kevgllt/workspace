entrada = input("Hoje está chovendo?\nSim ou Não\n: ")

def verifica_chuva(arg):
    if arg == 'S' or arg == 's' or arg == 'Sim' or arg == 'sim' or arg == 'SIM':
        return True
    elif arg == 'N' or arg == 'n' or arg == 'Nao' or arg == 'nao' or arg == 'NAO' or arg == 'Não' or arg == 'não' or arg == 'NÃO':
        return False
    else:
        return None

chuva_resultado = verifica_chuva(entrada)

def mensagem_chuva(arg):
    if arg:
        return f"Sim, leve seu guarda-chuva."
    elif arg == False:
        return f"Não, Sol muito forte."
    else:
        return f"ops! valores não permitidos."


print(f"{mensagem_chuva(chuva_resultado)}")
