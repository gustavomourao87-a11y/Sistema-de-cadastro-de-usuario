from sistema.entrada import pedir_cpf, pedir_nome
from sistema.banco import buscar_usuario, atualizar_usuario


def editar_usuario():

    cpf = pedir_cpf("Digite o CPF do usuário que deseja editar: ")

    usuario = buscar_usuario(cpf)

    if usuario:
        novo_nome = pedir_nome()

        atualizar_usuario(cpf, novo_nome)

        print("Usuário alterado com sucesso.")
        return

    print("CPF não cadastrado.")