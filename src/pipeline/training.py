from src.exception import FinanceException
from src.logger import logging as logger
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
from src.entity.artifact_entity import (DataIngestionArtifact)
from src.component.data_ingestion import DataIngestion


class TrainingPipeline:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.training_pipeline_config: TrainingPipelineConfig = training_pipeline_config

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            raise FinanceException(e, sys)