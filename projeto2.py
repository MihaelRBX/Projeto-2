def imprimeEscolhas():
    print("MACK BANK - ESCOLHA UMA OPCÃO")
    print("   (1)   CADASTRAR CONTA CORRENTE")
    print("   (2)   DEPOSITAR")
    print("   (3)   SACAR")
    print("   (4)   CONSULTAR SALDO")
    print("   (5)   CONSULTAR EXTRATO")
    print("   (6)   FINALIZAR")
    opcao = int(input("SUA OPCÃO: "))
    while opcao < 1 or opcao > 6:
        opcao = int(input("OPCÃO INVÁLIDA, INSIRA NOVAMENTE UMA OPCAO VÁLIDA: "))
    return opcao


imprimeEscolhas()