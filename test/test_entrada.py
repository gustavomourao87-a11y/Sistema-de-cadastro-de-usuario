from sistema.entrada import menu, pedir_cpf, pedir_nome

def test_pedir_cpf_valido(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "12345678900")

    resultado = pedir_cpf()

    assert resultado == "12345678900"

def test_pedir_cpf_invalido(monkeypatch):
    cpfs = iter(["123", "12345678900"])

    monkeypatch.setattr(
        "builtins.input", lambda _: next(cpfs)
        )

    resultado = pedir_cpf()

    assert resultado == "12345678900"

def test_pedir_nome_valido(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "Gustavo"
    )

    resultado = pedir_nome()

    assert resultado == "Gustavo"

def test_pedir_nome_invalido(monkeypatch):
    nomes = iter(["", "Gustavo"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(nomes)
    )

    resultado = pedir_nome()

    assert resultado == "Gustavo"

def test_pedir_cpf_com_letras(monkeypatch):
    cpfs = iter([
        "abc12345678",
        "12345678900"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(cpfs)
    )

    resultado = pedir_cpf()

    assert resultado == "12345678900"

def test_pedir_cpf_quantidade_invalida(monkeypatch):
    cpfs = iter([
        "123456",
        "12345678900"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(cpfs)
    )

    resultado = pedir_cpf()

    assert resultado == "12345678900"

def test_pedir_nome_com_espacos(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "  Gustavo  "
    )

    resultado = pedir_nome()

    assert resultado == "Gustavo"

def test_menu(monkeypatch, capsys):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1"
    )

    resultado = menu()

    capturado = capsys.readouterr()

    assert resultado == "1"
    assert "Sistema de Cadastro" in capturado.out

def test_menu_opcao_invalida(monkeypatch):
    opcoes = iter([
        "abc",
        "9",
        "1"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(opcoes)
    )

    resultado = menu()

    assert resultado == "1"