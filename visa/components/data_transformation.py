import os,sys 
import pandas as pd 
import numpy as np 
from visa.exception import CustomException
from visa.logger import logging
from visa.entity.config_entity import DataTransformationConfig
from visa.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact 
from sklearn.compose import ColumnTransformer 
from visa.utils.utils import read_yaml_file,load_data,save_numpy_array_data,save_object  
from visa.constant import * 
from sklearn.pipeline import Pipeline 
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import StandardScaler,OrdinalEncoder,OneHotEncoder,PowerTransformer
from imblearn.combine import SMOTTENN

class DataTransformation:
    def __init__(self,data_transformation_config:DataTransformationConfig,
                 data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_artifact:DataValidationArtifact):
        try:
            logging.info(f"{'>>'*30}Data Transformation log started.{'<<'*30}")
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
        
        except Exception as e:
            raise CustomException(e,sys) from e 
        
    def get_data_transformation_object(self)->ColumnTransformer:
        try:
            schema_file_path =self.data_validation_artifact.schema_file_path
            dataset_schema = read_yaml_file(file_path=schema_file_path) 
            
            numerical_columns = dataset_schema[NUMERICAL_COLUMN_KEY]
        except Exception as e:
            raise CustomException(e,sys) 