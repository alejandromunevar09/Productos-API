from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoUpdate


class ProductoRepository:
    """
    Capa de acceso a datos (DAL).
    Encapsula todas las operaciones de base de datos usando el ORM SQLAlchemy.
    No se escribe SQL manual: el ORM traduce todo a consultas automáticamente.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Producto]:
        """Obtiene todos los productos de la base de datos."""
        return self.db.query(Producto).all()

    def get_by_id(self, producto_id: int) -> Optional[Producto]:
        """Busca un producto por su identificador único."""
        return self.db.query(Producto).filter(Producto.id == producto_id).first()

    def create(self, producto_data: ProductoCreate) -> Producto:
        """Persiste un nuevo producto en la base de datos."""
        producto = Producto(**producto_data.model_dump())
        self.db.add(producto)
        self.db.commit()
        self.db.refresh(producto)
        return producto

    def update(self, producto_id: int, producto_data: ProductoUpdate) -> Optional[Producto]:
        """Actualiza los campos de un producto existente (solo los campos enviados)."""
        producto = self.get_by_id(producto_id)
        if not producto:
            return None
        # exclude_unset=True asegura que solo se actualicen los campos enviados
        update_data = producto_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(producto, key, value)
        self.db.commit()
        self.db.refresh(producto)
        return producto

    def delete(self, producto_id: int) -> bool:
        """Elimina un producto de la base de datos. Retorna True si fue eliminado."""
        producto = self.get_by_id(producto_id)
        if not producto:
            return False
        self.db.delete(producto)
        self.db.commit()
        return True
