from cgitb import handler
from dataclasses import dataclass


@dataclass
class AccountsConfig:
    MINIO_STORAGE_URL: str
    MINIO_STORAGE_BUCKET: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str


@dataclass
class HandelerConfig:
    push: bool
    path_file_up: str
    path_file_in: str
    path_file_save: str
    content_type: str


@dataclass
class PushPullConfig:
    accounts: AccountsConfig
    handeler: HandelerConfig