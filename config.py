from dataclasses import dataclass

from environs import Env


@dataclass
class db_type:
    dbname: str
    user: str
    password: str


@dataclass
class Config:
    db: db_type


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        db=db_type(
            dbname=env.str("DBNAME"),
            user=env.str("DB_USER"),
            password=env.str("DB_PASSWORD")
        )
    )
