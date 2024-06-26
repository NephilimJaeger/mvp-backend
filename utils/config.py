from environs import Env

envconfig = Env()

class Config:
    POSTGRES_USER = envconfig("POSTGRES_USER")
    POSTGRES_PW = envconfig("POSTGRES_PW")
    POSTGRES_URL = envconfig("POSTGRES_URL")

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}"

