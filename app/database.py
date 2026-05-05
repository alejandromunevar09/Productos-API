from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a SQLite (base de datos local, sin configuración adicional)
SQLALCHEMY_DATABASE_URL = "sqlite:///./productos.db"

# Motor de base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necesario para SQLite con FastAPI
)

# Fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos ORM
Base = declarative_base()


# Dependencia de inyección de sesión para los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
