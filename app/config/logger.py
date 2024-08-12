import logging
import os

from app.utils.utils import update_envs

logging.basicConfig(level=logging.INFO)


def setup_logger(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )
    logger = logging.getLogger(__name__)
    return logger


update_envs(override_vars=["LOG_LEVEL"])
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logger = setup_logger(level=getattr(logging, log_level))
