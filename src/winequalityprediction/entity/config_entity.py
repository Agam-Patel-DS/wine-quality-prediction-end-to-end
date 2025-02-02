from dataclasses import dataclass
from pathlib import Path

#Dataclass - we don't have to use self keyword and is just used to assign data not functions

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema:dict

@dataclass
class DataTransformationConfig:
    root_dir:Path
    data_path: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str