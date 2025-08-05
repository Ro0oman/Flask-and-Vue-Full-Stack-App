import os

class Config:
    # Lee la URL de la base de datos de las variables de entorno.
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_URL', None)

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No se ha configurado la variable de entorno POSTGRES_URL")

    # SQLAlchemy espera 'postgresql' en lugar de 'postgres'
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False