import os,sys 
from visa.constant import * 
from visa.logger import logging
from visa.exception import CustomException
from visa.entity.config_entity import * 
from visa.utils.utils import read_yaml_file 
from visa.entity.config_entity import DataIngestionConfig,DataValidationConfig
from visa.entity.artifact_entity import DataIngestionArtifact 
from visa.config.configuration import Configuration 
from datetime import date 
import pandas as pd 
import numpy as np 
from six.moves import urllib
from sklearn.model_selection import train_test_split 

class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_config:DataIngestionConfig):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys) from e 
        