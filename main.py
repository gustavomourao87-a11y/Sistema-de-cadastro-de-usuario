from sistema.entrada import menu
from sistema.cadastro import cadastrar_usuario

while True:
    opcao = menu()
    if opcao == "1":
      cadastrar_usuario()
    elif opcao =="0":
       break