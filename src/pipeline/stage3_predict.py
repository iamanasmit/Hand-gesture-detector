from src.components.predict import Predictor
from src.config import ConfigManager

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        c=ConfigManager()
        predict_conf=c.get_predict_config()
        p=Predictor(predict_conf)
        p.estimate()