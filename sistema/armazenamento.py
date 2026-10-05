import json
from sistema.usuario import Usuario

def carregar_usuarios():
    try:
        with open("dados/usuarios.json", "r") as arquivo:
            dados = json.load(arquivo)

            usuarios = []

            for usuario in dados:
                usuarios.append(
                    Usuario(usuario["nome"], usuario["cpf"])
                )

            return usuarios

    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")
        return []

    except json.JSONDecodeError:
        print("O arquivo de usuários está inválido.")
        return []        

def salvar_usuarios(usuarios):
    try:
        with open("dados/usuarios.json", "w") as arquivo:

            dados = []

            for usuario in usuarios:
                dados.append({
                    "nome": usuario.nome,
                    "cpf": usuario.cpf
                })

            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    except OSError:
        print("Não foi possível salvar os usuários.")