from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from utils.config import Config

pg_conn_string = Config.SQLALCHEMY_DATABASE_URI

def create_db_engine(conn_string):
    engine = create_engine(conn_string, echo=True)
    return engine

def db_init(engine):
    if not database_exists(engine.url):
        try:
            create_database(engine.url)
            print('Database created')
        except Exception as e:
            print(f'Error creating database: {e}')
    else:
        print('Database already exists')

def connect_to_db(engine):
    connection = engine.connect()
    return connection


engine = create_db_engine(pg_conn_string)
db_init(engine) 

connection = connect_to_db(engine)
Session = sessionmaker(bind=engine)
session = Session()


# stmt = select(Aluno.nome)

# with session as sess:
#     result = sess.execute(stmt)
#     for aluno in result:
#         print(aluno[0])