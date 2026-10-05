from sistema.cadastro import usuarios
from sistema.entrada import pedir_cpf

def excluir_usuario():
    cpf = pedir_cpf()
    verificar = False

    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            usuarios.remove(usuario)
            print("Usuário removido com sucesso.")
            verificar = True
            break
    if not verificar:
        print("Usuário não cadastrado.")