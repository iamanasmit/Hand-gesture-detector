from src.entity import PrepareBaseModelConfig, PreprocessConfig, PredictConfig
from src.utils import read_yaml, create_directories
from src.constants import CONFIG_FILE_PATH, PARAM_FILE_PATH
from pathlib import Path

class ConfigManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        param_filepath=PARAM_FILE_PATH):

        self.config=read_yaml(config_filepath)
        self.param=read_yaml(param_filepath)

        create_directories(self.config.artifacts_root)

    def get_base_model_configs(self)->PrepareBaseModelConfig:
        base_model_config=self.config.prepare_base_model

        model_config=PrepareBaseModelConfig(
            root_dir=Path(base_model_config.root_dir),
            base_model_path=Path(base_model_config.base_model_path),
            updated_base_model_path=Path(base_model_config.updated_base_model_path),
            params_image_size=self.param.IMAGE_SIZE,
            params_classes=self.param.CLASSES
        )
        
        return model_config
    
    def get_preprocess_config(self)->PreprocessConfig:
        create_directories(self.config.preprocess_data.preprocessed_data_dir)

        PreprocessConfigObj=PreprocessConfig(
            data_path= self.config.data_root,
            preprocessed_data_dir= self.config.preprocess_data.preprocessed_data_dir,
            image_tensor_path=self.config.preprocess_data.image_tensors_path,
            labels_path= self.config.preprocess_data.labels_path,
            image_size= self.param.IMAGE_SIZE,
            classes= self.param.CLASSES
        )

        return PreprocessConfigObj
    
    def get_predict_config(self):
        predict_config_obj=PredictConfig(
            prediction_dir=self.config.prediction.prediction_dir,
            trained_model_path=self.config.prediction.trained_model_path,
            image_size=self.param.IMAGE_SIZE
        )

        return predict_config_obj