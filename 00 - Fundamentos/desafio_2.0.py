saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

continuar = 1

while continuar == 1:

    menu = int(input('''

[1] Depositar
[2] Sacar
[3] Extrato


=> '''))

    transformacao = str(menu)

    if transformacao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print('Depósito realizando.')
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif transformacao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print("Saque realizado.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif transformacao == "3":
        print("\n================ EXTRATO ================")
        if extrato:
            print("\n".join(extrato))
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    continuar = int(input('''
Voçê quer fazer mais alguma operação?

[1] Sim
[2] Não

=> '''))

    if continuar == 2:
        print("Saindo... Obrigado por usar nosso banco!")
    elif continuar != 1:
        print("Opção inválida. Saindo por segurança.")
        break
