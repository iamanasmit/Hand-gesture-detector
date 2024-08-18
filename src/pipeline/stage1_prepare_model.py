from src.components.create_model import PrepareBaseModel
from src.config import ConfigManager

class CreateModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        con_generator=ConfigManager()
        model_config=con_generator.get_base_model_configs()
        p=PrepareBaseModel(model_config)
        p.create_model()