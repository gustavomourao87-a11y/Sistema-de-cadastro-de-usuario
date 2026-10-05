from sistema.dados import usuarios
from sistema.entrada import pedir_cpf


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("==== LISTA DE USUÁRIOS ====")
    print()

    for usuario in usuarios:
        print("Nome:", usuario["nome"])
        print("CPF:", usuario["cpf"])
        print("------------------")


def consultar_usuario():
    cpf = pedir_cpf()

    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print("Nome:", usuario["nome"])
            print("CPF:", usuario["cpf"])
            return

    print("Usuário não cadastrado.")