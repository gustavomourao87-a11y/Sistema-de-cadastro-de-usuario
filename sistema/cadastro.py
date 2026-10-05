from sistema.entrada import pedir_nome, pedir_cpf
usuarios = []
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
        if not verificar:
            continue
        break
        

    novo_usuario = {
    "nome": nome,
    "cpf": cpf

    }

    usuarios.append(novo_usuario)

    print("Usuário cadastrado com sucesso!")