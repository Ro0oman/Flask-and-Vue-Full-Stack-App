from pathlib import Path

class Config:
    SQLALCHEMY_DATABASE_URI= 'sqlite:///' + str(BASE_DIR.joinpath('db.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False