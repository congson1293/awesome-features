from utils.configs import PushPullConfig
from utils.minio_handle import push_file, pull_file
import hydra


@hydra.main(config_path="configs", config_name="config")
def main(cfg: PushPullConfig):
    if cfg.handeler.push:
        assert (isinstance(cfg.handeler.path_file_up, str) and isinstance(cfg.handeler.path_file_in, str) and isinstance(cfg.handeler.content_type, str))
        push_file(cfg.accounts, cfg.handeler.path_file_in, cfg.handeler.path_file_up, cfg.handeler.content_type)
    else: # pull
        assert (isinstance(cfg.handeler.path_file_up, str) and isinstance(cfg.handeler.path_file_save, str))
        pull_file(cfg.accounts, cfg.handeler.path_file_up, cfg.handeler.path_file_save)

if __name__=='__main__':
    main()
