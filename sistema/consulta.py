from sistema.cadastro import usuarios
from sistema.entrada import pedir_cpf

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
          
def consultar_usuario():
    cpf =pedir_cpf()
    verificar = False
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print("nome: ", usuario["nome"])
            print("CPF:", usuario["cpf"])
            verificar = True
    if not verificar:
        print("Usuário não cadastrado.")
