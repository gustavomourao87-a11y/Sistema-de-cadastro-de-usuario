import json
from sistema.armazenamento import carregar_usuarios, salvar_usuarios


def test_carregar_usuarios(tmp_path, monkeypatch):
    pasta_dados = tmp_path / "dados"
    pasta_dados.mkdir()

    arquivo = pasta_dados / "usuarios.json"

    arquivo.write_text(
        '[{"nome": "Gustavo", "cpf": "12345678900"}]',
        encoding="utf-8"
    )

    monkeypatch.chdir(tmp_path)

    resultado = carregar_usuarios()

    assert resultado == [
        {
            "nome": "Gustavo",
            "cpf": "12345678900"
        }
    ]

def test_carregar_usuarios_arquivo_nao_encontrado(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    resultado = carregar_usuarios()

    capturado = capsys.readouterr()

    assert resultado == []
    assert "Arquivo de usuários não encontrado." in capturado.out

def test_carregar_usuarios_json_invalido(tmp_path, monkeypatch, capsys):
    pasta_dados = tmp_path / "dados"
    pasta_dados.mkdir()

    arquivo = pasta_dados / "usuarios.json"

    arquivo.write_text(
        "JSON inválido",
        encoding="utf-8"
    )

    monkeypatch.chdir(tmp_path)

    resultado = carregar_usuarios()

    capturado = capsys.readouterr()

    assert resultado == []
    assert "O arquivo de usuários está inválido." in capturado.out

def test_salvar_usuarios(tmp_path, monkeypatch):
    pasta_dados = tmp_path / "dados"
    pasta_dados.mkdir()

    monkeypatch.chdir(tmp_path)

    usuarios = [
        {
            "nome": "Gustavo",
            "cpf": "12345678900"
        }
    ]

    salvar_usuarios(usuarios)

    arquivo = pasta_dados / "usuarios.json"

    assert arquivo.exists()

    dados_salvos = json.loads(
        arquivo.read_text(encoding="utf-8")
    )

    assert dados_salvos == usuarios

def test_salvar_usuarios_erro(monkeypatch, capsys):
    def abrir_com_erro(*args, **kwargs):
        raise OSError

    monkeypatch.setattr(
        "builtins.open",
        abrir_com_erro
    )

    salvar_usuarios([])

    capturado = capsys.readouterr()

    assert "Não foi possível salvar os usuários." in capturado.out