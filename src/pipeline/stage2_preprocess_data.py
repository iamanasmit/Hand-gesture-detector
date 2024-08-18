from src.components.preprocess import Preprocess
from src.config import ConfigManager

class PreprocessPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        c=ConfigManager()
        preprocess_config=c.get_preprocess_config()
        p=Preprocess(preprocess_config)
        p.process()