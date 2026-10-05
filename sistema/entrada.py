def menu():
    print("==== Sistema de Cadastro ====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuário")
    print("3 - Buscar usuário ")
    print("4 - Editar usuário ")
    print("5 - Excluir usuário")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")
    return opcao

def pedir_nome():
    while True:
        nome = input("Digite o nome do usuário que deseja cadastrar: ").strip
        if not nome:
            print("Não é possivel deixar vazio.")
            continue
        return nome

def pedir_cpf():
    while True:
        cpf = input("Digite o CPF do usuário que deseja cadastrar: ").strip()
        if len(cpf) != 11 or not cpf.isdigit():
         print("CPF precisa ter 11 números.")
         continue
        return cpf




