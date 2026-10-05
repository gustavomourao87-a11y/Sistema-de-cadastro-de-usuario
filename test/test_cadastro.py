from sistema.cadastro import cadastrar_usuario
from sistema.dados import usuarios

def test_cadastrar_usuario(monkeypatch):
    usuarios.clear()

    dados = iter([
        "Gustavo",
        "12345678900"
        ])

    monkeypatch.setattr(
        "builtins.input", lambda _: next(dados)
        )
    monkeypatch.setattr(
        "sistema.cadastro.salvar_usuarios", lambda _: None
    )

    cadastrar_usuario()

    assert usuarios[-1]["nome"] == "Gustavo"
    assert usuarios[-1]["cpf"] ==  "12345678900"

def test_cadastrar_cpf_duplicado(monkeypatch):
    usuarios.clear()

    usuarios.append({
        "nome": "João",
        "cpf": "12345678900"
    })

    dados = iter([
        "Gustavo",
        "12345678900",
        "98765432100"
    ])

    monkeypatch.setattr(
        "builtins.input", lambda _: next(dados)
    )

    monkeypatch.setattr(
        "sistema.cadastro.salvar_usuarios", lambda _: None
    )

    cadastrar_usuario()

    assert usuarios[-1]["nome"] == "Gustavo"
    assert usuarios[-1]["cpf"] == "98765432100"