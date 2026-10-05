from sistema.entrada import menu
from sistema.cadastro import cadastrar_usuario
from sistema.consulta import listar_usuarios, consultar_usuario
from sistema.edicao import editar_usuario
from sistema.exclusao import excluir_usuario
from sistema.armazenamento import carregar_usuarios
from sistema.dados import usuarios


def main():
    usuarios.extend(carregar_usuarios())

    while True:
        opcao = menu()

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            consultar_usuario()

        elif opcao == "4":
            editar_usuario()

        elif opcao == "5":
            excluir_usuario()

        elif opcao == "0":
            break


if __name__ == "__main__":
    main()