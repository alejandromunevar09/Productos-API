from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import productos

# Crear tablas automáticamente al iniciar (SQLAlchemy ORM)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Productos",
    description="""
## Backend RESTful con FastAPI + SQLAlchemy

Aplicación desarrollada para la **Unidad 2 - Arquitectura de Aplicaciones Web**.

### Operaciones disponibles
- **GET** `/api/v1/productos/` — Listar todos los productos
- **GET** `/api/v1/productos/{id}` — Obtener un producto por ID
- **POST** `/api/v1/productos/` — Crear un nuevo producto
- **PUT** `/api/v1/productos/{id}` — Actualizar un producto existente
- **DELETE** `/api/v1/productos/{id}` — Eliminar un producto

### Stack tecnológico
- **Framework**: FastAPI (Python)
- **ORM**: SQLAlchemy
- **Base de datos**: SQLite (local)
- **Validación**: Pydantic v2
    """,
    version="1.0.0",
    contact={
        "name": "Arquitectura de Aplicaciones Web - Unidad 2",
    }
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro del router de productos
app.include_router(productos.router)


@app.get("/", tags=["Root"], summary="Estado de la API")
def root():
    """Endpoint de verificación de estado de la API."""
    return {
        "message": "API de Productos activa",
        "version": "1.0.0",
        "docs": "/docs",
        "framework": "FastAPI",
        "orm": "SQLAlchemy",
        "database": "SQLite"
    }
