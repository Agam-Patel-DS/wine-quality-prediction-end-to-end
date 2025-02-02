import os
from src.winequalityprediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.winequalityprediction.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config

    # To perform the train test split
    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)
        train, test=train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(f"Train Shape: {train.shape}")
        logger.info(f"Test Shape: {test.shape}")

        print(train.shape)
        print(test.shape)
