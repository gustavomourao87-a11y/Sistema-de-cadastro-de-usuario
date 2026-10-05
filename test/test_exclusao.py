from sistema.exclusao import excluir_usuario
from sistema.dados import usuarios


def test_excluir_usuario(monkeypatch):
    usuarios.clear()

    usuarios.append({
        "nome": "João",
        "cpf": "12345678900"
    })

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "12345678900"
    )

    monkeypatch.setattr(
        "sistema.exclusao.salvar_usuarios",
        lambda _: None
    )

    excluir_usuario()

    assert len(usuarios) == 0

def test_excluir_usuario_nao_cadastrado(monkeypatch, capsys):
    usuarios.clear()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99999999999"
    )

    monkeypatch.setattr(
        "sistema.exclusao.salvar_usuarios",
        lambda _: None
    )

    excluir_usuario()

    capturado = capsys.readouterr()

    assert "Usuário não cadastrado." in capturado.out