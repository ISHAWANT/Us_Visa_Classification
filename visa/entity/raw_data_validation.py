from visa.pipeline.pipeline import Pipeline 
from visa.exception import CustomException 
from visa.logger import logging 
from visa.config.configuration import Configuration 
from visa.components.data_ingestion import DataIngestion 
import os,sys 
import json 
from visa.utils.utils import read_yaml_file 

class IngestedDataValidation:
    def __init__(self,validate_path,schema_path):
        try:
            pass 
        except Exception as e:
            raise CustomException(e,sys) from e 
        
    def validate_file_name():
        pass 
    def validate_columns_length():
        pass 
    def missing_values_columns():
        pass 
    
    