from sistema.entrada import pedir_nome, pedir_cpf
usuarios = []
def cadastrar_usuario():
    nome = pedir_nome()
    cpf = pedir_cpf()

    novo_usuario = {
    "nome": nome,
    "cpf": cpf

    }

    usuarios.append(novo_usuario)

    print("Usuário cadastrado com sucesso!")