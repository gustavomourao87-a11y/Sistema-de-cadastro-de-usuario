from sistema.entrada import pedir_cpf, pedir_nome

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