import os

import bcrypt
from dotenv import dotenv_values


def verify_password(plain_password, hashed_password):
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)


def update_envs(override_vars: list[str]):
    env_vars = dotenv_values(
        "./.env",
    )
    for var in override_vars:
        if var in env_vars:
            os.environ[var] = env_vars[var]
