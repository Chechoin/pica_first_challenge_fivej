from sqlalchemy import Column, Date, Integer, String

from .config.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    fecha = Column(Date)
    hashed_password = Column(String(255))
