from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from app.config.logger import Logger


async def custom_exception_handler(request: Request, exc: Exception):
    logger = Logger().logger
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )
    else:
        logger.error(f"Error: {exc}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"message": f"An internal server error occurred. {exc}"},
        )
