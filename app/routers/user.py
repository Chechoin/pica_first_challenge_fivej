from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.config.database import get_db
from app.config.logger import Logger
from app.services import crud

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user.email)
    logger = Logger().logger
    if db_user:
        logger.debug("Email already registered")
        raise HTTPException(status_code=400, detail="Email already registered")
    logger.info("Creating a new user")
    created_user = crud.create_user(db=db, user=user)
    logger.info(f"User created: {created_user}")
    return created_user


@router.put("/users/{user_id}", response_model=schemas.User)
def update_user_endpoint(
    user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)
):
    logger = Logger().logger
    logger.info(f"Updating user with ID {user_id}")
    db_user = crud.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        logger.debug(f"User with ID {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    logger = Logger().logger
    logger.debug("** ** ** DEBUG MESSAGE!")
    logger.info("** ** ** INFO MESSAGE!")
    logger.warning("** ** ** WARNING MESSAGE!")
    logger.error("** ** ** ERROR MESSAGE!")
    logger.critical("** ** ** CRITICAL MESSAGE!")

    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        logger.debug(f"User with ID {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
