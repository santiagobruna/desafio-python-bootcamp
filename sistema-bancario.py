def mostra_menu():
    menu = """
        =============== BANCO SANT ===============

        [1] - Depositar
        [2] - Sacar - (valor máximo: R$ 500)
        [3] - Exibir Extrato
        [4] - Sair
        
        Obrigado por fazer parte do BANCO SANT.
        ====================================
        
        =>
    """
    return input(menu).strip()

def depositar(saldo, extrato, numero_depositos):
    deposito = float(input("Digite o valor do depósito:"))
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        numero_depositos += 1
        print("Depósito feito com sucesso!")
    else:
        print("Erro! Valor inválido para depósito.")
    return saldo, extrato, numero_depositos

def sacar(saldo, limite_saque, numero_saques, extrato):
    valor_saque = float(input("Digite o valor do saque:"))
    if(numero_saques >= 3):
        print("Você atingiu o limite diário de 3 saques")
    else:
        if valor_saque > limite_saque:
            print("Erro. Limite máximo de saque R$ 500.")
        elif valor_saque > saldo :
            print("Operação falhou! Você não tem saldo suficiente.")
        else:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
    return saldo, numero_saques, extrato

def exibir_extrato(saldo, extrato, numero_saques, numero_depositos):
    if extrato == "":
        print("Não foram realizadas movimentações")
    else:
        print("\n================ EXTRATO ================")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"\nTotal Saques: {numero_saques}")
        print(f"\nTotal Depósitos: {numero_depositos}")
        print("==========================================")

def main():
    saldo = 0
    limite_saque = 500
    numero_saques = 0
    numero_depositos = 0
    extrato = ""
    while True:
        opcao = mostra_menu()

        if opcao == "1":
            saldo, extrato, numero_depositos = depositar(saldo, extrato, numero_depositos)
        elif opcao == "2":
            saldo, numero_saques, extrato = sacar(saldo, limite_saque, numero_saques, extrato)
        elif opcao == "3":
            exibir_extrato(saldo, extrato, numero_saques, numero_depositos)
        elif opcao == "4":
            print("Saindo do programa...")
            break
    print("Encerrando Programa...")
    print("Programa encerrado.....")

# Executa apenas se o arquivo for rodado diretamente
if __name__ == "__main__":
    main()