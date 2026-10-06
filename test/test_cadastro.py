from sistema.cadastro import cadastrar_usuario


def test_cadastrar_usuario(monkeypatch):

    dados = iter([
        "Gustavo",
        "12345678900"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(dados)
    )

    monkeypatch.setattr(
        "sistema.cadastro.buscar_usuario",
        lambda cpf: None
    )

    resultado = []

    monkeypatch.setattr(
        "sistema.cadastro.inserir_usuario",
        lambda nome, cpf: resultado.append((nome, cpf))
    )

    cadastrar_usuario()

    assert resultado == [
        ("Gustavo", "12345678900")
    ]

def test_cadastrar_cpf_duplicado(monkeypatch):

    dados = iter([
        "Gustavo",
        "12345678900",
        "98765432100"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(dados)
    )

    usuarios_banco = {
        "12345678900": ("João", "12345678900")
    }

    def buscar(cpf):
        return usuarios_banco.get(cpf)

    monkeypatch.setattr(
        "sistema.cadastro.buscar_usuario",
        buscar
    )

    resultado = []

    monkeypatch.setattr(
        "sistema.cadastro.inserir_usuario",
        lambda nome, cpf: resultado.append((nome, cpf))
    )

    cadastrar_usuario()

    assert resultado == [
        ("Gustavo", "98765432100")
    ]