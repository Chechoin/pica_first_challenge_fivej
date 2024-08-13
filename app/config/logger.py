import logging
import os

from app.utils.utils import update_envs


class Logger:
    def __init__(self):
        update_envs(override_vars=["LOG_LEVEL", "LOG_FORMAT"])
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        log_format = os.getenv(
            "LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self.logger = self.setup_logger(
            log_format=log_format,
            level=getattr(logging, log_level),
        )

    def setup_logger(self, log_format, level=logging.INFO):
        # Obtén el logger con un nombre único (en lugar de __name__)
        logger = logging.getLogger(__name__)

        # Elimina todos los manejadores existentes si hay alguno
        while logger.hasHandlers():
            logger.removeHandler(logger.handlers[0])

        # Configura el logger nuevamente
        logger.setLevel(level)
        handler = logging.StreamHandler()

        # Usa el formato proporcionado o un formato predeterminado
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger
