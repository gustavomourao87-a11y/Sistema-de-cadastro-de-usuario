from sistema.cadastro import usuarios

def listar_usuarios():

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("==== LISTA DE USUÁRIOS ====")
    print("")
    for usuario in usuarios:   
        print("nome", usuario["nome"])
        print("cpf", usuario["cpf"])
        print("------------------")
          
        