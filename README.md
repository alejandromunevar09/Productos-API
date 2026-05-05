# API de Productos - Backend RESTful

> Actividad Sumativa | Unidad 2 | Arquitectura de Aplicaciones Web

## Stack Tecnológico

| Componente | Tecnología |
|---|---|
| Framework | FastAPI (Python) |
| ORM | SQLAlchemy |
| Base de datos | SQLite (local) |
| Validación | Pydantic v2 |
| Servidor | Uvicorn (ASGI) |
| Documentación | Swagger UI (integrado) |

## Arquitectura del proyecto

```
productos-api/
├── app/
│   ├── main.py                          # Punto de entrada, configuración FastAPI
│   ├── database.py                      # Conexión y sesión SQLAlchemy
│   ├── models/
│   │   └── producto.py                  # Modelo ORM → tabla en BD
│   ├── schemas/
│   │   └── producto.py                  # Schemas Pydantic (validación/serialización)
│   ├── repositories/
│   │   └── producto_repository.py       # Capa de acceso a datos (DAL)
│   ├── services/
│   │   └── producto_service.py          # Capa de lógica de negocio (BLL)
│   └── routers/
│       └── productos.py                 # Endpoints RESTful (controladores)
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación y ejecución

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/productos-api.git
cd productos-api

# 2. Crear entorno virtual
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar el servidor
uvicorn app.main:app --reload
```

## Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/productos/` | Listar todos los productos |
| GET | `/api/v1/productos/{id}` | Obtener producto por ID |
| POST | `/api/v1/productos/` | Crear nuevo producto |
| PUT | `/api/v1/productos/{id}` | Actualizar producto |
| DELETE | `/api/v1/productos/{id}` | Eliminar producto |

## Documentación interactiva (Swagger)

Con el servidor en ejecución, acceder a:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Ejemplo de payload (POST/PUT)

```json
{
  "nombre": "Laptop Dell XPS 15",
  "descripcion": "Laptop de alto rendimiento con pantalla OLED 4K",
  "precio": 4500000.00
}
```
