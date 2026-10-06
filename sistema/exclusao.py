from sistema.entrada import pedir_cpf
from sistema.banco import buscar_usuario, excluir_usuario as excluir_usuario_banco


def excluir_usuario():

    cpf = pedir_cpf("Digite o CPF do usuário que deseja excluir: ")

    usuario = buscar_usuario(cpf)

    if usuario:
        excluir_usuario_banco(cpf)

        print("Usuário removido com sucesso.")
        return

    print("Usuário não cadastrado.")