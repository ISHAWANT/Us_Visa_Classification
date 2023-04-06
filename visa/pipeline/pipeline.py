import sys 
from visa.constant import * 
from visa.logger import logging
from visa.exception import CustomException
from visa.entity.config_entity import * 
from visa.utils.utils import read_yaml_file
from visa.components.data_ingestion import DataIngestion
from visa.entity.artifact_entity import DataIngestionArtifact
from visa.config.configuration import Configuration
#data Validation
from visa.components.data_ingestion import DataIngestion
from visa.components.data_validation import DataValidationArtifact
#data transformation
from visa.components.data_transformation import DataTransformationArtifact
from visa.components.data_transformation import DataTransformation
from visa.components.data_validation import DataValidation
#Model trainer
from visa.components.model_trainer import ModelTrainer 
from visa.entity.artifact_entity import ModelTrainerArtifact


class Pipeline():

    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise CustomException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e, sys) from e 
        
# Data Validation 

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),data_ingestion_artifact=data_ingestion_artifact)
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise CustomException(e,sys) from e 
        
    def satrt_data_transformation(self,data_ingestion_artifact:DataIngestionArtifact,
                                  data_validation_artifact:DataValidationArtifact)->DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.config.get_data_transformation_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            return data_transformation.initiate_data_transformation() 
        except Exception as e:
            raise CustomException(e,sys) from e 
        
    #Model trainer 
    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(model_trainer_config=self.config.get_model_traineer_config(),
                                         data_transformation_artifact=data_transformation_artifact)
            return model_trainer.initiate_model_trainer()
        
        except Exception as e:
            raise CustomException(e,sys) 
        
    
    def run_pipeline(self):                                                   
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            #data Validation 
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            #Data Transformation 
            data_transformation_artifact = self.satrt_data_transformation(data_ingestion_artifact=data_ingestion_artifact,
                                                                          data_validation_artifact=data_validation_artifact)
        except Exception as e:
            raise CustomException(e,sys) from e 


        
        
            
            
        