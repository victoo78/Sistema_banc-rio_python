import textwrap

def menu():
    menu_texto = """\n
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair
    => """
    return input(textwrap.dedent(menu_texto))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Operação falhou: valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print("❌ Valor excede o limite por saque.")
    elif numero_saques >= limite_saques:
        print("❌ Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")
    else:
        print("❌ Valor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("❌ Já existe usuário com esse CPF.")
        return

    nome = input("Nome completo: ").strip()
    nascimento = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ").strip()

    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("✅ Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print("✅ Conta criada com sucesso!")
    else:
        print("❌ Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        print("=" * 30)
        print(f"Agência: {conta['agencia']}")
        print(f"Conta:   {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print("=" * 30)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("✅ Obrigado por usar o sistema bancário!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
import textwrap

def menu():
    menu_texto = """\n
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair
    => """
    return input(textwrap.dedent(menu_texto))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Operação falhou: valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print("❌ Valor excede o limite por saque.")
    elif numero_saques >= limite_saques:
        print("❌ Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")
    else:
        print("❌ Valor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("❌ Já existe usuário com esse CPF.")
        return

    nome = input("Nome completo: ").strip()
    nascimento = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ").strip()

    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("✅ Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print("✅ Conta criada com sucesso!")
    else:
        print("❌ Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        print("=" * 30)
        print(f"Agência: {conta['agencia']}")
        print(f"Conta:   {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print("=" * 30)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("✅ Obrigado por usar o sistema bancário!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
