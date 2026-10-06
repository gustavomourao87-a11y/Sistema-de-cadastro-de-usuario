import sqlite3


def conectar_banco():
    conexao = sqlite3.connect("dados/usuarios.db")
    return conexao


def criar_tabela():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE
        )
    """)

    conexao.commit()
    conexao.close()

def inserir_usuario(nome, cpf):
    conexao = conectar_banco()

    conexao.execute("""
        INSERT INTO usuarios (nome, cpf)
            VALUES (?, ?)
    """,(nome, cpf) )
    conexao.commit()
    conexao.close()

def buscar_usuario(cpf):
    conexao = conectar_banco()

    resultado = conexao.execute("""
        SELECT * FROM usuarios
        WHERE cpf = ?
    """, (cpf,)).fetchone()

    conexao.close()

    return resultado

def atualizar_usuario(cpf, novo_nome):
    conexao = conectar_banco()

    conexao.execute("""
        UPDATE usuarios
        SET nome = ?
        WHERE cpf = ?
    """, (novo_nome, cpf))

    conexao.commit()
    conexao.close()

def excluir_usuario(cpf):
    conexao = conectar_banco()

    conexao.execute("""
        DELETE FROM usuarios
        WHERE cpf = ?
    """, (cpf,))

    
    conexao.commit()
    conexao.close()

def buscar_todos_usuarios():
    conexao = conectar_banco()

    usuarios = conexao.execute("""
        SELECT * FROM usuarios
    """).fetchall()

    conexao.close()

    return usuarios

if __name__ == "__main__":
    criar_tabela()