#entrada = input("O dia está chuvoso?\nSim ou Não\n\nEntrada: ")

nome_usuario = input("Informe seu nome:\nEntrada: ")
sobrenome_usuario = input("\nInforme seu sobrenome:\nEntrada: ")


def saudar_usuario(nome, sobrenome):
    return f"\nBem-vindo mestre {nome} {sobrenome}"


print(
    saudar_usuario(nome_usuario, sobrenome_usuario)
)
