from src.winequalityprediction.config.configuration import ConfigurationManager
from src.winequalityprediction.components.data_transformation import DataTransformation
from src.winequalityprediction import logger
from pathlib import Path
STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status=f.read().split(" ")
            if status[-1] == "True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("Your data scheme is not valid!")
            
        except Exception as e:
            raise e
