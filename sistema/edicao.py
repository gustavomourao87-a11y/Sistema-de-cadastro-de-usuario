from sistema.dados import usuarios
from sistema.entrada import pedir_cpf, pedir_nome
from sistema.armazenamento import salvar_usuarios

def editar_usuario():
    cpf = pedir_cpf()
    verificar = False
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            novo_nome = pedir_nome()
            usuario["nome"] = novo_nome
            salvar_usuarios(usuarios)
            print("Usuário alterado com sucesso.")
            verificar = True
    if not verificar:
        print("CPF não cadastrado.")