from flask import Flask
from utils.config import Config

pg_conn_string = Config.SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = pg_conn_string


