import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

class Settings:
    # URL do banco de dados (utilizando a variável de ambiente)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    
    # URL do Redis (opcional, se você estiver usando o Redis)
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Chave secreta para autenticação (usado por exemplo para JWT)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    
    # Outras configurações, se necessário
    # Exemplo: tempo de expiração de sessões ou logs
    SESSION_EXPIRATION: int = os.getenv("SESSION_EXPIRATION", 3600)

# Instância das configurações
settings = Settings()
