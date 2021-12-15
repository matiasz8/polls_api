import os
from typing import Dict

from starlette.config import Config

ROOT_DIR = os.getcwd()
_config = Config(os.path.join(ROOT_DIR, '.env'))
APP_VERSION = "0.0.1"
APP_NAME = "Pools App"
API_PREFIX = "/v1"

# Env vars
IS_DEBUG: bool = _config("IS_DEBUG", cast=bool, default=True)

# ENV
ENV: str = _config("ENV", cast=str, default="")
