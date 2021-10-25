from dataclasses import dataclass

import yaml


@dataclass
class Config:
    n_epochs: int
    batch_size: int
    train_filename: str
    valid_filename: str

    @classmethod
    def load(cls, config_path: str) -> "Config":
        with open(config_path) as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)
        
        return cls(**config)
