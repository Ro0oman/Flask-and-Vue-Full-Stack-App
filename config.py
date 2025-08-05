import os

class Config:
    # Lee la URL de la base de datos de las variables de entorno.
    # Vercel la inyectará automáticamente como POSTGRES_URL.
    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_URL')
    # SQLAlchemy espera 'postgresql' en lugar de 'postgres'
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False