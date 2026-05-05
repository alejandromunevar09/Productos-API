from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, status
from app.repositories.producto_repository import ProductoRepository
from app.schemas.producto import ProductoCreate, ProductoUpdate, ProductoResponse


class ProductoService:
    """
    Capa de lógica de negocio (BLL).
    Orquesta operaciones del repositorio y aplica reglas de negocio.
    También gestiona el manejo de errores con respuestas HTTP apropiadas.
    """

    def __init__(self, db: Session):
        self.repository = ProductoRepository(db)

    def get_all_productos(self) -> List[ProductoResponse]:
        """Retorna todos los productos disponibles."""
        return self.repository.get_all()

    def get_producto_by_id(self, producto_id: int) -> ProductoResponse:
        """Retorna un producto por ID. Lanza 404 si no existe."""
        producto = self.repository.get_by_id(producto_id)
        if not producto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con id '{producto_id}' no encontrado."
            )
        return producto

    def create_producto(self, producto_data: ProductoCreate) -> ProductoResponse:
        """Crea y retorna un nuevo producto."""
        return self.repository.create(producto_data)

    def update_producto(self, producto_id: int, producto_data: ProductoUpdate) -> ProductoResponse:
        """Actualiza y retorna el producto modificado. Lanza 404 si no existe."""
        producto = self.repository.update(producto_id, producto_data)
        if not producto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con id '{producto_id}' no encontrado."
            )
        return producto

    def delete_producto(self, producto_id: int) -> dict:
        """Elimina un producto. Lanza 404 si no existe."""
        deleted = self.repository.delete(producto_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con id '{producto_id}' no encontrado."
            )
        return {"message": f"Producto con id '{producto_id}' eliminado exitosamente."}
