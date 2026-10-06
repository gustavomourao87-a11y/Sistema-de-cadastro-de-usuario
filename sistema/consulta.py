from sistema.dados import usuarios
from sistema.entrada import pedir_cpf


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("==== LISTA DE USUÁRIOS ====")
    print()

    for usuario in usuarios:
       print(usuario.exibir_dados())
       print("------------------")


def consultar_usuario():
    cpf = pedir_cpf("Digite o CPF do usuário que deseja consultar: ")

    for usuario in usuarios:
        if cpf == usuario.cpf:
            print(usuario.exibir_dados())
            return

    print("Usuário não cadastrado.")