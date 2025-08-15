from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import settings

# Definindo a base para os modelos
Base = declarative_base()

# Criando o engine de conexão com o banco de dados
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL  # Usando a URL do banco de dados do arquivo config.py

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Criando a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
