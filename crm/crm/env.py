from pathlib import Path 
from functools import lru_cache
from decouple import config as decouple_config,Config,RepositoryEnv
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR=BASE_DIR.parent
ENIV_PATH_DIR=PROJECT_DIR/".env"

@lru_cache()
def get_config():
    if ENIV_PATH_DIR.exists():
        return Config(RepositoryEnv(str(ENIV_PATH_DIR)))
    return decouple_config

config=get_config()

