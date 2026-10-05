from sistema.dados import usuarios
from sistema.entrada import pedir_cpf
from sistema.armazenamento import salvar_usuarios

def excluir_usuario():
    cpf = pedir_cpf()
    verificar = False

    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            usuarios.remove(usuario)
            salvar_usuarios(usuarios)
            print("Usuário removido com sucesso.")
            verificar = True
            break
    if not verificar:
        print("Usuário não cadastrado.")