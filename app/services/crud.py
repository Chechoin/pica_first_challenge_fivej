import bcrypt
from sqlalchemy.orm import Session

from .. import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    db_user = models.User(
        email=user.email,
        nombre=user.nombre,
        apellido=user.apellido,
        fecha=user.fecha,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate) -> models.User:
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    db_user.email = user.email
    db_user.nombre = user.nombre
    db_user.apellido = user.apellido
    db_user.fecha = user.fecha
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, user_email: int) -> models.User:
    db_user = db.query(models.User).filter(models.User.email == user_email).first()
    return db_user
