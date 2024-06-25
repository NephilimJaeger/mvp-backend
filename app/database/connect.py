from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from config import Config

from models import Aluno

pg_conn_string = Config.SQLALCHEMY_DATABASE_URI

def connect_to_db(conn_string):
    engine = create_engine(conn_string, echo=True)
    connection = engine.connect()

    return connection

connection = connect_to_db(pg_conn_string)
session = Session(connection)

stmt = select(Aluno.nome)

with session as sess:
    result = sess.execute(stmt)
    for aluno in result:
        print(aluno[0])