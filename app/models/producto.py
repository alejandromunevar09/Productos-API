from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Producto(Base):
    """
    Entidad Producto mapeada a la tabla 'productos' en la base de datos.
    SQLAlchemy (ORM) se encarga de crear la tabla automáticamente.
    """
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=True)
    precio = Column(Float, nullable=False)
