from sistema.entrada import pedir_nome, pedir_cpf
from sistema.dados import usuarios
from sistema.armazenamento import salvar_usuarios
from sistema.usuario import Usuario


def cadastrar_usuario():
    nome = pedir_nome()

    while True:
        verificar = False

        cpf = pedir_cpf("Digite o CPF do usuário que deseja cadastrar: ")

        for usuario in usuarios:
            if cpf == usuario["cpf"]:
                print("CPF já cadastrado.")
                verificar = True
                break

        if verificar:
            continue

        break

    novo_usuario = Usuario(nome, cpf)

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")