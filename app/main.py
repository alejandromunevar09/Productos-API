from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import productos

# Unidad 3: importar la app GraphQL de Ariadne
from app.graphql.router import graphql_app

# Crear tablas automáticamente al iniciar (SQLAlchemy ORM)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Productos",
    description="""
## Backend RESTful + GraphQL con FastAPI + SQLAlchemy

Aplicación desarrollada para las **Unidades 2 y 3 - Arquitectura de Aplicaciones Web**.

### API REST — Unidad 2
- **GET** `/api/v1/productos/` — Listar todos los productos
- **GET** `/api/v1/productos/{id}` — Obtener un producto por ID
- **POST** `/api/v1/productos/` — Crear un nuevo producto
- **PUT** `/api/v1/productos/{id}` — Actualizar un producto existente
- **DELETE** `/api/v1/productos/{id}` — Eliminar un producto

### API GraphQL — Unidad 3
- **GET** `/graphql` — Playground interactivo GraphiQL
- **POST** `/graphql` — Ejecutar queries y mutations

### Stack tecnológico
- **Framework**: FastAPI (Python)
- **ORM**: SQLAlchemy
- **Base de datos**: SQLite (local)
- **Validación**: Pydantic v2
- **GraphQL**: Ariadne (schema-first con SDL)
    """,
    version="2.0.0",
    contact={
        "name": "Arquitectura de Aplicaciones Web - Unidades 2 y 3",
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

# ── Unidad 2: Router REST ──────────────────────────────────────────────────────
app.include_router(productos.router)

# ── Unidad 3: Endpoint GraphQL ────────────────────────────────────────────────
# GET  /graphql → abre el playground GraphiQL en el navegador
# POST /graphql → ejecuta queries y mutations como JSON
app.mount("/graphql", graphql_app)


@app.get("/", tags=["Root"], summary="Estado de la API")
def root():
    """Endpoint de verificación de estado de la API."""
    return {
        "message": "API de Productos activa",
        "version": "2.0.0",
        "rest_docs": "/docs",
        "graphql_playground": "/graphql",
        "framework": "FastAPI",
        "graphql_libreria": "Ariadne (schema-first SDL)",
        "orm": "SQLAlchemy",
        "database": "SQLite"
    }
