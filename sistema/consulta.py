from sistema.banco import buscar_usuario, buscar_todos_usuarios
from sistema.entrada import pedir_cpf


def listar_usuarios():
    usuarios = buscar_todos_usuarios()

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("==== LISTA DE USUÁRIOS ====")
    print()

    for usuario in usuarios:
        print(f"Nome: {usuario[1]}")
        print(f"CPF: {usuario[2]}")
        print("------------------")


def consultar_usuario():
    cpf = pedir_cpf("Digite o CPF do usuário que deseja consultar: ")

    usuario = buscar_usuario(cpf)

    if usuario:
        print(f"Nome: {usuario[1]}")
        print(f"CPF: {usuario[2]}")
        return

    print("Usuário não cadastrado.")