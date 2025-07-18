def menu():
    return """
    
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Novo usuário
    [6] Sair
    
    => """

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, n_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = n_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        n_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, n_saques

def historico(saldo,/,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_conta(agencia, n_conta, usuarios):
    cpf = int(input('Digite seu CPF: '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return {'agencia': agencia, 'numero_conta': n_conta, 'usuario': usuario}
    else:
        print('Não foi possivel criar a conta.')

def novo_usuario(usuarios):
    nome = input('Digite o seu nome: ')
    nascimento = int(input('Digite a sua data de nascimento: '))
    cpf = int(input('Digite seu CPF: '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('O CPF digitado já está vinculado a um usúario. ')
        return
    print('\n=============ENDEREÇO=============')
    logradouro = input('Digite seu logradouro: ')
    numero = input('Digite o número: ')
    bairro = input('Digite o seu bairro: ')
    cidade = input('Digite a cidade que você mora: ')
    endereco = f"{logradouro}, {numero}, {bairro}, {cidade}"
    usuarios.append({
        'Nome': nome,
        'Nascimento': nascimento,
        'CPF': cpf,
        'Endereço': endereco
    })

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            return usuario
    return None


def principal():
    agencia = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    n_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    n_conta = 0

    while True:

        opcao = input(menu())

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, n_saques = sacar(
                saldo= saldo,
                valor = valor,
                extrato=extrato,
                limite=limite,
                n_saques=n_saques,
                limite_saques=limite_saques
            )

        elif opcao == "3":
            historico(saldo, extrato=extrato)

        elif opcao == "4":
            conta = criar_conta(agencia, n_conta, usuarios)

            if conta:
                contas.append(conta)
                n_conta += 1

        elif opcao == "5":
            novo_usuario(usuarios)

        elif opcao == "6":
            print("Saindo... Obrigado por utilizar nosso sistema!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

principal()
