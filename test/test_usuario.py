from sistema.usuario import Usuario


def test_criar_usuario():
    usuario = Usuario("Gustavo", "12345678900")

    assert usuario.nome == "Gustavo"
    assert usuario.cpf == "12345678900"

def test_exibir_dados():
    usuario = Usuario("Gustavo", "12345678900")

    resultado = usuario.exibir_dados()

    assert resultado == "Nome: Gustavo | CPF: 12345678900"

def test_criar_dois_usuarios():
    usuario1 = Usuario("Gustavo", "12345678900")
    usuario2 = Usuario("João", "98765432100")

    assert usuario1.nome == "Gustavo"
    assert usuario2.nome == "João"

    assert usuario1.cpf == "12345678900"
    assert usuario2.cpf == "98765432100"

def test_usuario_nome_vazio():
    try:
        Usuario("", "12345678900")
        assert False
    except ValueError:
        assert True

def test_usuario_cpf_vazio():
    try:
        Usuario("Gustavo", "")
        assert False
    except ValueError:
        assert True

def test_usuario_cpf_invalido():
    try:
        Usuario("Gustavo", "123")
        assert False
    except ValueError:
        assert True

def test_alterar_nome():
    usuario = Usuario("João", "12345678900")

    usuario.alterar_nome("Gustavo")

    assert usuario.nome == "Gustavo"