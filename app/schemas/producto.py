from pydantic import BaseModel, Field
from typing import Optional


class ProductoBase(BaseModel):
    """Campos comunes compartidos entre creación y respuesta."""
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del producto")
    descripcion: Optional[str] = Field(None, max_length=500, description="Descripción breve del producto")
    precio: float = Field(..., gt=0, description="Precio del producto (debe ser mayor a 0)")


class ProductoCreate(ProductoBase):
    """Schema para crear un nuevo producto (POST)."""
    pass


class ProductoUpdate(BaseModel):
    """Schema para actualizar un producto (PUT). Todos los campos son opcionales."""
    nombre: Optional[str] = Field(None, min_length=1, max_length=100, description="Nombre del producto")
    descripcion: Optional[str] = Field(None, max_length=500, description="Descripción breve del producto")
    precio: Optional[float] = Field(None, gt=0, description="Precio del producto")


class ProductoResponse(ProductoBase):
    """Schema de respuesta que incluye el id generado por la base de datos."""
    id: int

    class Config:
        from_attributes = True  # Permite mapear desde objetos ORM a Pydantic
