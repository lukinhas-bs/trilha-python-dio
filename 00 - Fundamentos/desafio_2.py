def depositar(saldo, valor, extrato): #retorne saldo e extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print('Depósito realizando.')
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

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

    return saldo, extrato, numero_saques

def historico(saldo,/, *, extrato):
    print("\n================ EXTRATO ================")
    if extrato:
        print("\n".join(extrato))
    else:
        print("Não foram realizadas movimentações.")

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario (usuario):

    nome = input("Digite o seu nome: ")
    data = int(input("Digite a sua data do seu nascimento: " ))
    cpf = int(input('Digite o seu CPF: '))

    for u in usuario:
        if u["CPF"] == cpf:
            print("Esse CPF já foi cadastrado.")
            return

    print("\n=============ENDEREÇO=============")
    rua = input("Digite a rua que voçê mora: ")
    bairro = input("Digite o seu bairro: ")
    numero = input("Digite o número: ")
    cidade = input("Digite a cidade que você mora: ")
    estado = input("Digite o estado que você mora: ")
    endereco = f"{rua}, {bairro}, {numero}, {cidade},{estado}"
    usuario.append({"Nome": nome, "Nascimento": data, "CPF": cpf, "Endereço": endereco})
    print('Usuário criado')

def criar_conta(agencia, n_conta, usuario):

    cpf = int(input("Digite o seu CPF: "))
    if usuario:
        print("Conta criada.")
        return {"agencia": agencia, "numero_conta": n_conta, "usuario": usuario}
    else:
        print("Não foi possivel criar a conta.")

def principal():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    limite_saques = 3
    usuario = []
    contas = []
    agencia = 1
    n_conta = 0

    continuar = 1

    while continuar == 1:
        menu = int(input('''

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta

    => '''))

        transformacao = str(menu)

        if transformacao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif transformacao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,
            numero_saques=numero_saques,limite_saques=limite_saques)

        elif transformacao == "3":
            historico(saldo, extrato=extrato)

        elif transformacao == "4":
            criar_usuario(usuario)

        elif transformacao == "5":
            conta = criar_conta(agencia, n_conta, usuario)
            if conta:
                contas.append(conta)
                n_conta += 1
                agencia += 1

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

        continuar = int(input('''
Você quer fazer mais alguma operação?

[1] Sim
[2] Não

=> '''))

        if continuar == 2:
            print("Saindo... Obrigado por usar nosso banco!")
            break
        elif continuar != 1:
            print("Opção inválida. Saindo por segurança.")
            break

principal()
