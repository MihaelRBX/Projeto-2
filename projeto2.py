def cadastrar_conta_corrente():
    print("Você escolheu a opção para cadastro de conta corrente.")


def depositar():
    print("Você escolheu a opção de depositar.")


def sacar():
    print("Você escolheu a opção de sacar.")


def consultar_saldo():
    print("Você escolheu a opção para consulta de saldo.")


def consultar_extrato():
    print("Você escolheu a opção para consulta de extrato.")


def finalizar():
    print("Você escolheu a opção para finalizar o programa.")


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
        opcao = int(input("OPCÃO INVÁLIDA, INSIRA UMA OPCAO VÁLIDA: "))
    
    if opcao == 1:
        cadastrar_conta_corrente()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4:
        consultar_saldo()
    elif opcao == 5:
        consultar_extrato()
    elif opcao == 6:
        finalizar()