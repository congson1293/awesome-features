#from django.conf import settings
from minio import Minio
from io import BytesIO
from datetime import timedelta

from utils.configs import AccountsConfig

class MinioHandler:
    __instance = None

    @staticmethod
    def get_instance(cfg):
        """ Static access method. """
        if not MinioHandler.__instance:
            MinioHandler.__instance = MinioHandler(cfg)
        return MinioHandler.__instance

    def __init__(self, cfg: AccountsConfig):
        self.cfg = cfg
        self.minio_url = cfg.MINIO_STORAGE_URL
        self.access_key = cfg.MINIO_ACCESS_KEY
        self.secret_key = cfg.MINIO_SECRET_KEY
        self.bucket_name = cfg.MINIO_STORAGE_BUCKET
        self.client = Minio(
            self.minio_url,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False,
        )
        self.make_bucket()

    def make_bucket(self) -> str:
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)
        return self.bucket_name

    def presigned_get_object(self, bucket_name, object_name):
        # Request URL expired after 7 days
        url = self.client.presigned_get_object(
            bucket_name=bucket_name,
            object_name=object_name,
            expires=timedelta(days=7)
        )
        return url

    def check_file_name_exists(self, bucket_name, file_name):
        try:
            self.client.stat_object(
                bucket_name=bucket_name, object_name=file_name)
            return True
        except Exception as e:
            print(f'[x] Exception: {e}')
            return False

    def put_object(self, file_data, file_name, content_type):
        try:
            self.client.put_object(
                bucket_name=self.bucket_name,
                object_name=file_name,
                data=file_data,
                content_type=content_type,
                length=-1,
                part_size=10 * 1024 * 1024
            )
            url = self.presigned_get_object(
                bucket_name=self.bucket_name, object_name=file_name)
            data_file = {
                'bucket_name': self.bucket_name,
                'file_name': file_name,
                'url': url
            }
            return data_file
        except Exception as e:
            raise Exception(e)

    def get_file_minio(self, file_name):
        try:
            minio_client = self.get_instance(self.cfg)
            file = minio_client.client.get_object(
                minio_client.bucket_name, file_name).read()
            return file
        except Exception as e:
            print(e)

    def save_file_minio(self, blob, img_name):
        save_file = self.get_instance(self.cfg).put_object(
            file_name=img_name,
            file_data=BytesIO(blob),
            content_type="image/jpeg"
        )
        return save_file


def push_file(cfg: AccountsConfig, path_file_in: str, path_file_up: str, content_type: str):
    """Upload file to server

    Args:
        cfg (AccountsConfig): account config
        path_file_in (str): path to file to upload
        path_file_up (str): path to save file in mino
        content_type (str): check content_type (gg keyword i.e. wav mime type)
    """
    handler = MinioHandler(cfg)

    file = open(path_file_in, 'rb')
    handler.get_instance(cfg).put_object(file_name=path_file_up,
                                      file_data=file, content_type=content_type)


def pull_file(cfg: AccountsConfig, path_file_up: str, path_file_save: str):
    """Pull file from server

    Args:
        cfg (AccountsConfig): account config
        path_file_up (str): path file saved in mino
        path_file_save (str): path file saved in local machine
    """
    handler = MinioHandler(cfg)
    downloaded = handler.get_file_minio(path_file_up)
    with open(path_file_save, 'wb') as f:
        f.write(downloaded)
