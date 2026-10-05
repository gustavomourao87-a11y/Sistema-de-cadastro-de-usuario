from sistema.entrada import menu
from sistema.cadastro import cadastrar_usuario
from sistema.consulta import listar_usuarios

while True:
    opcao = menu()
    if opcao == "1":
      cadastrar_usuario()
    elif opcao == "2":
       listar_usuarios()
    elif opcao == "0":
       break