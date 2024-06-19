import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="../configs", config_name="main")
def app(cfg : DictConfig = None) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(cfg.db.password)
    print(cfg['db']['password'])
    print(cfg.db.age)
    print(cfg.db.current_age)
    print(cfg.db.age_string)


if __name__ == "__main__":
    app()