from src.winequalityprediction.config.configuration import ConfigurationManager
from src.winequalityprediction.components.model_evaluation import ModelEvaluation
from src.winequalityprediction import logger

STAGE_NAME = "Model Evaluation Stage"

class Model_EvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
