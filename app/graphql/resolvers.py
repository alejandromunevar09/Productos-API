# =============================================================================
# Resolvers GraphQL — Unidad 3 - Arquitectura de Aplicaciones Web
#
# Un resolver es una función que obtiene los datos reales para cada campo
# definido en el schema. Ariadne ejecuta el resolver correspondiente por cada
# campo que el cliente solicita en su consulta.
# =============================================================================
from ariadne import QueryType, MutationType
from sqlalchemy.orm import Session
from app.models.producto import Producto as ProductoModel

query = QueryType()
mutation = MutationType()


# ── Query Resolvers ────────────────────────────────────────────────────────────

@query.field("productos")
def resolve_productos(_, info):
    db: Session = info.context["db"]
    return db.query(ProductoModel).all()


@query.field("producto")
def resolve_producto(_, info, id):
    db: Session = info.context["db"]
    return db.query(ProductoModel).filter(ProductoModel.id == int(id)).first()


# ── Mutation Resolvers ─────────────────────────────────────────────────────────

@mutation.field("crearProducto")
def resolve_crear_producto(_, info, input):
    db: Session = info.context["db"]
    nuevo = ProductoModel(
        nombre=input["nombre"],
        descripcion=input.get("descripcion"),
        precio=input["precio"]
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@mutation.field("actualizarProducto")
def resolve_actualizar_producto(_, info, id, input):
    db: Session = info.context["db"]
    producto = db.query(ProductoModel).filter(ProductoModel.id == int(id)).first()
    if not producto:
        return None
    for campo, valor in input.items():
        if valor is not None:
            setattr(producto, campo, valor)
    db.commit()
    db.refresh(producto)
    return producto


@mutation.field("eliminarProducto")
def resolve_eliminar_producto(_, info, id):
    db: Session = info.context["db"]
    producto = db.query(ProductoModel).filter(ProductoModel.id == int(id)).first()
    if not producto:
        return False
    db.delete(producto)
    db.commit()
    return True