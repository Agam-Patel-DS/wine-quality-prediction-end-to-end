from src.winequalityprediction.config.configuration import ConfigurationManager
from src.winequalityprediction.components.data_validation import DataValidation
from src.winequalityprediction import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()