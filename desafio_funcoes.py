menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lu] Listar Usuários
[lc] Listar Contas
[q] Sair

=> """

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    agencia = "0001"
    numero_conta = 0

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            imprimirExtrato(saldo, extrato=extrato)

        elif opcao == "nu":
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ")
            criarUsuario(usuarios, nome, data_nascimento, cpf, endereco)

        elif opcao == "nc":
            if usuarios == []:
                print("Nenhum usuário cadastrado! Por favor, crie um usuário antes de criar uma conta.")
                continue
            cpf = input("CPF (somente números): ")
            for usuario in usuarios:
                if usuario["cpf"] == cpf:
                    criarConta(agencia, numero_conta, usuarios, cpf)
                    numero_conta += 1
                else: 
                    print("Usuário não encontrado, por favor crie um usuário antes de criar uma conta.")

        elif opcao == "lu":
            listarUsuarios(usuarios)
        
        elif opcao == "lc":
            listarContas(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def criarUsuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado com esse CPF!")
            return
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "contas": []
    })

def criarConta(agencia, numero_conta, usuarios, cpf):
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta + 1,
        "usuario": usuarios['cpf']
    }
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario['contas'].append(conta)
        return True
    print("Usuário não encontrado!")
    return False

def listarUsuarios(usuarios):
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Data de Nascimento: {usuario['data_nascimento']}, Endereço: {usuario['endereco']}")

def listarContas(usuarios, numero_conta):
    if numero_conta == 0:   
        print("Nenhuma conta cadastrada.")
        return
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return
    for usuario in usuarios:
        if len(usuario['contas']):
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}:")
            print(f" Contas:")
            for conta in usuario['contas']:
                print(f"  Agência: {conta['agencia']}, Conta: {conta['numero_conta']}")
                print("")

def imprimirExtrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

if __name__ == "__main__":
    main()