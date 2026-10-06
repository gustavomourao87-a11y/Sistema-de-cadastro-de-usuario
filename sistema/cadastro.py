from sistema.entrada import pedir_nome, pedir_cpf
from sistema.banco import inserir_usuario, buscar_usuario


def cadastrar_usuario():
    nome = pedir_nome()

    while True:
        cpf = pedir_cpf(
            "Digite o CPF do usuário que deseja cadastrar: "
        )

        usuario = buscar_usuario(cpf)

        if usuario:
            print("CPF já cadastrado.")
            continue

        break

    inserir_usuario(nome, cpf)

    print("Usuário cadastrado com sucesso!")