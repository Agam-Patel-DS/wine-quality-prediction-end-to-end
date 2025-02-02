from src.winequalityprediction import logger
from src.winequalityprediction.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
logger.info("Custom Logging Intialised Successfully!")

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> {STAGE_NAME} Started! <<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> {STAGE_NAME} Completed! <<<<<")
except Exception as e:
    logger.exception(e)
    raise e