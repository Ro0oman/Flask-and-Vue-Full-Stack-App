from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
print(BASE_DIR)

class Config:
    SQLALCHEMY_DATABASE_URI= 'sqlite:///' + str(BASE_DIR.joinpath('db.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave-super-secreta'
