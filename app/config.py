from environs import Env

envconfig = Env()


class Config:
    SQLALCHEMY_DATABASE_URI = envconfig.str("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
