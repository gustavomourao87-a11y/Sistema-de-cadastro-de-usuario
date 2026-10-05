from sistema.entrada import pedir_nome
usuarios = []
def cadastrar_usuario():
    usuario = pedir_nome()

    novo_usuario = {
    "nome": usuario
    }

    usuarios.append(novo_usuario)