from sistema.entrada import pedir_nome, pedir_cpf
from sistema.dados import usuarios
from sistema.armazenamento import salvar_usuarios

def cadastrar_usuario():
    nome = pedir_nome()
    verificar = False
    while True:
        cpf = pedir_cpf()

        for usuario in usuarios:
            if cpf == usuario["cpf"]:
                print("CPF já cadastrado.")
                verificar = True
                break
            
        if verificar:
            continue
        break
        

    novo_usuario = {
    "nome": nome,
    "cpf": cpf

    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")