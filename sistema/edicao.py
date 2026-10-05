from sistema.cadastro import usuarios
from sistema.entrada import pedir_cpf, pedir_nome

def editar_usuario():
    cpf = pedir_cpf()
    verificar = False
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            novo_nome = pedir_nome()
            usuario["nome"] = novo_nome
            print("Usuário alterado com sucesso.")
            verificar = True
    if not verificar:
        print("CPF não cadastrado.")