import os,sys 
from visa.constant import * 
from visa.logger import logging
from visa.exception import CustomException
from visa.entity.config_entity import * 
from visa.utils.utils import read_yaml_file 
from visa.entity.config_entity import DataIngestionConfig,DataValidationConfig
from visa.entity.artifact_entity import DataIngestionArtifact ,DataValidationArtifact
from visa.config.configuration import Configuration 
from datetime import date 
import pandas as pd 
import numpy as np 
from six.moves import urllib
from sklearn.model_selection import train_test_split 
from visa.entity.raw_data_validation import IngestedDataValidation

class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info(">>> Data Validation log started >>>")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.schema_path = self.data_validation_config.Schema_file_path 
            self.train_data = IngestedDataValidation(
                validate_path=self.data_ingestion_artifact.train_file_path,schema_path=self.schema_path   
            ) 
            self.test_data = IngestedDataValidation(
                validate_path=self.data_ingestion_artifact.test_file_path,schema_path=self.schema_path
            )
        except Exception as e:
            raise CustomException(e,sys) from e 
    def isFolderPathAvailable(self)->bool:
        try:
            is_folder_available=False
            train_path = self.data_ingestion_artifact.train_file_path
            test_path = self.data_ingestion_artifact.test_file_path 
            
            if os.path.exists(train_path):
                if os.path.exists(test_path):
                    is_folder_available=True
            return is_folder_available
        except Exception as e:
            raise CustomException(e,sys) from e 
    
    def isValidation_successful(self):
        try:
            validation_status=True 
            if self.isFolderPathAvailable()==True:
                train_file_name = os.path.basename(self.data_ingestion_artifact.train_file_path) 
                is_train_filename_validated = self.train_data.validate_filename(train_file_name=train_file_name) 
                is_train_column_numbers_validated = self.train_data.validate_column_length() 
                is_train_column_name_same = self.train_data.check_column_names()
                is_train_missing_values_whole_column = self.train_data.missing_values_whole_column() 
                self.train_data.replace_null_values_with_null() 
                
                test_file_name = os.path.basename(self.data_ingestion_artifact.test_file_path)
                is_test_file_name_validated = self.test_data.validate_filename(file_name=test_file_name) 
                is_test_columns_numbers_validated = self.test_data.validate_column_length() 
                is_test_column_name_same = self.test_data.check_column_names() 
                is_test_missing_values_whole_column = self.test_data.missing_values_whole_column() 
                self.test_data.replace_null_values_with_null() 
                
                if is_train_filename_validated & is_train_column_numbers_validated & is_train_column_name_same & is_test_missing_values_whole_column:
                    pass 
                else:
                    validation_status = False 
                    logging.info("Check your training data validation failed. ")
                    raise ValueError('Check your training data, Validation Failed')  
                if is_test_file_name_validated & is_test_columns_numbers_validated & is_test_column_name_same & is_test_missing_values_whole_column:
                    pass
                else:
                    validation_status = False
                    logging.info("Check your testing data validation failed. ")
                    raise ValueError('Check your testing data,validation Failded')
                
        except Exception as e:
            raise CustomException(e,sys) from e 
                
    def initiate_data_validation(self):
        try:
            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.schema_path,is_validated=self.isValidation_successful(),
                message='Data Validation performed'
            )
            logging.info(f"Data Validation Artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise CustomException(e,sys) from e 
    
    def __del__(self):
        logging.info(f"<<<<<<<<<<<<<< Data Validation log completed >>>>>>>>>>>>>>>>") 