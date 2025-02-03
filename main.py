from src.winequalityprediction import logger
from src.winequalityprediction.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.winequalityprediction.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.winequalityprediction.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.winequalityprediction.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.winequalityprediction.pipeline.model_evaluation_pipeline import Model_EvaluationPipeline
logger.info("Custom Logging Intialised Successfully!")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"\n>>>>> {STAGE_NAME} Started! <<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"\n>>>>> {STAGE_NAME} Completed! <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"\n>>>>> {STAGE_NAME} Started! <<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f"\n>>>>> {STAGE_NAME} Completed! <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"\n>>>>> {STAGE_NAME} Started! <<<<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f"\n>>>>> {STAGE_NAME} Completed! <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"\n>>>>> {STAGE_NAME} Started! <<<<<")
    model_trainer=ModelTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f"\n>>>>> {STAGE_NAME} Completed! <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"\n>>>>> {STAGE_NAME} Started! <<<<<")
    model_evaluator=Model_EvaluationPipeline()
    model_evaluator.initiate_model_evaluation()
    logger.info(f"\n>>>>> {STAGE_NAME} Completed! <<<<<")
except Exception as e:
    logger.exception(e)
    raise e