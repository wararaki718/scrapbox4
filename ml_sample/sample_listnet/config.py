from dataclasses import dataclass

import yaml


@dataclass
class Config:
    n_train: int
    n_valid: int
    n_input: int
    n_epochs: int
    batch_size: int

    @classmethod
    def load(cls, config_path: str) -> "Config":
        with open(config_path) as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)
        
        return cls(**config)
