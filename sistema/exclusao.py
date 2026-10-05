from sistema.dados import usuarios
from sistema.entrada import pedir_cpf
from sistema.armazenamento import salvar_usuarios


def excluir_usuario():
    cpf = pedir_cpf()

    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            usuarios.remove(usuario)
            salvar_usuarios(usuarios)

            print("Usuário removido com sucesso.")
            return

    print("Usuário não cadastrado.")