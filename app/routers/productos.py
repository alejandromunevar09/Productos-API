from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.producto import ProductoCreate, ProductoUpdate, ProductoResponse
from app.services.producto_service import ProductoService

router = APIRouter(
    prefix="/api/v1/productos",
    tags=["Productos"]
)


@router.get(
    "/",
    response_model=List[ProductoResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar todos los productos",
    description="Retorna la lista completa de productos registrados en la base de datos."
)
def get_all_productos(db: Session = Depends(get_db)):
    service = ProductoService(db)
    return service.get_all_productos()


@router.get(
    "/{producto_id}",
    response_model=ProductoResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener un producto por ID",
    description="Retorna un producto específico buscado por su identificador único."
)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    service = ProductoService(db)
    return service.get_producto_by_id(producto_id)


@router.post(
    "/",
    response_model=ProductoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo producto",
    description="Registra un nuevo producto en la base de datos y retorna el objeto creado con su ID generado."
)
def create_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    service = ProductoService(db)
    return service.create_producto(producto)


@router.put(
    "/{producto_id}",
    response_model=ProductoResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar un producto",
    description="Actualiza uno o más campos de un producto existente identificado por su ID."
)
def update_producto(producto_id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    service = ProductoService(db)
    return service.update_producto(producto_id, producto)


@router.delete(
    "/{producto_id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar un producto",
    description="Elimina permanentemente un producto de la base de datos identificado por su ID."
)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    service = ProductoService(db)
    return service.delete_producto(producto_id)
