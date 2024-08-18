from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_classes: int

@dataclass(frozen= True)
class PreprocessConfig:
    data_path: Path
    preprocessed_data_dir: Path
    image_tensor_path: Path
    labels_path: Path
    image_size: list
    classes: int

@dataclass(frozen=True)
class PredictConfig:
    prediction_dir: Path
    trained_model_path: Path
    image_size: list