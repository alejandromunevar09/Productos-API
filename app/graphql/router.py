# =============================================================================
# Integración de Ariadne con FastAPI — Unidad 3
#
# make_executable_schema combina el SDL (type_defs) con los resolvers Python
# para generar el schema GraphQL ejecutable.
#
# GraphQLWithDB extiende la clase GraphQL de Ariadne para inyectar la sesión
# de SQLAlchemy en el contexto de cada request, permitiendo que los resolvers
# accedan a la base de datos sin acoplamientos directos.
# =============================================================================

from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from app.database import SessionLocal
from app.graphql.schema import type_defs
from app.graphql.resolvers import query, mutation

schema = make_executable_schema(type_defs, [query, mutation])


def get_context(request) -> dict:
    db = SessionLocal()
    return {
        "request": request,
        "db": db
    }


graphql_app = GraphQL(schema, context_value=get_context, debug=True)
