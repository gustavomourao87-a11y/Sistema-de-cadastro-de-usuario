from sistema.dados import usuarios
from sistema.entrada import pedir_cpf, pedir_nome
from sistema.armazenamento import salvar_usuarios


def editar_usuario():

    cpf = pedir_cpf("Digite o CPF do usuário que deseja editar: ")

    for usuario in usuarios:
        if cpf == usuario.cpf:
            novo_nome = pedir_nome()

            usuario.alterar_nome(novo_nome)

            salvar_usuarios(usuarios)

            print("Usuário alterado com sucesso.")
            return

    print("CPF não cadastrado.")