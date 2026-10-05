import json

def carregar_usuarios():
    with open("dados/usuarios.json", "r") as arquivo:
        usuario = json.load(arquivo)

    return usuario
def salvar_usuarios(usuarios):
    with open("dados/usuarios.json" "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)