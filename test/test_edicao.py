from sistema.edicao import editar_usuario
from sistema.dados import usuarios


def test_editar_usuario(monkeypatch):
    usuarios.clear()

    usuarios.append({
        "nome": "João",
        "cpf": "12345678900"
    })

    dados = iter([
        "12345678900",
        "Gustavo"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(dados)
    )

    monkeypatch.setattr(
        "sistema.edicao.salvar_usuarios",
        lambda _: None
    )

    editar_usuario()

    assert usuarios[0]["nome"] == "Gustavo"
    assert usuarios[0]["cpf"] == "12345678900"

def test_editar_usuario_nao_cadastrado(monkeypatch, capsys):
    usuarios.clear()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99999999999"
    )

    editar_usuario()

    capturado = capsys.readouterr()

    assert "CPF não cadastrado." in capturado.out