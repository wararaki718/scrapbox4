from dataclasses import dataclass

import yaml


@dataclass
class AsymmetricCosineKNNConfig:
    top_k: int
    shrinkage: float
    feature_weighting: str
    alpha: float


@dataclass
class IALSConfig:
    n_components: int
    alpha: float
    reg: float
    max_epoch: int


@dataclass
class Config:
    asymmetric_cosine_knn_config: AsymmetricCosineKNNConfig
    ials_config: IALSConfig

    @classmethod
    def load(cls, config_path: str) -> "Config":
        with open(config_path) as f:
            config = yaml.safe_load(f)
        
        return cls(
            asymmetric_cosine_knn_config=AsymmetricCosineKNNConfig(**config["AsymmetricCosineKNN"]),
            ials_config=IALSConfig(**config["IALS"])
        )
