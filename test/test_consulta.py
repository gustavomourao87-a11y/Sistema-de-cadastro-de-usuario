from sistema.consulta import consultar_usuario
from sistema.dados import usuarios

def test_consultar_usuario(monkeypatch, capsys):
    usuarios.clear()

    usuarios.append({
        "nome": "João",
        "cpf": "12345678900"
    })

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "12345678900"
    )

    consultar_usuario()

    capturado = capsys.readouterr()

    assert "João" in capturado.out
    assert "12345678900" in capturado.out

def test_consultar_usuario_nao_cadastrado(monkeypatch, capsys):
    usuarios.clear()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99999999999"
    )

    consultar_usuario()

    capturado = capsys.readouterr()

    assert "Usuário não cadastrado." in capturado.out