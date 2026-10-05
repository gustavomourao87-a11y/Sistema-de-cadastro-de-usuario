import json

def carregar_usuarios():
    try:
        with open("dados/usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

            return usuarios
        
    except FileNotFoundError:
         print("Arquivo de usuários não encontrado.")
         return []
    except json.JSONDecodeError:
         print("O arquivo de usuários está inválido.")
         return []
        

    return usuario
def salvar_usuarios(usuarios):
    try:
        with open("dados/usuarios.json" "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

    except OSError:
        print("Não foi possível salvar os usuários.")