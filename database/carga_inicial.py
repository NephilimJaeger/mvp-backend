from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError


def executa_sql_script(conn, file_path):
    """
    Lê e executa comandos SQL de um arquivo especificado.

    :param conn: A conexão do SQLAlchemy com o banco de dados.
    :param file_path: O caminho para o arquivo SQL a ser executado.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as sql_file:
            sql_commands = sql_file.read()
            for command in sql_commands.strip().split(";"):
                if command.strip():
                    conn.execute(text(command.strip()))
    except Exception as e:
        print(f"Erro ao executar o arquivo SQL {file_path}: {e}")
        raise


def db_carga_inicial(conn):
    """
    Executa comandos SQL dos arquivos para criar tabelas e inserir dados.

    :param conn: Conexão do SQLAlchemy com o banco de dados.
    """
    try:
        with conn.begin() as transaction:
            try:
                executa_sql_script(conn, "database/create_tables.sql")
                executa_sql_script(conn, "database/inserts.sql")
                print("Tabelas criadas e dados inseridos com sucesso.")
            except Exception as e:
                transaction.rollback()
                print(f"Erro ao executar comandos SQL: {e}")
                raise
    except SQLAlchemyError as e:
        print(f"Erro ao executar arquivos SQL: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
