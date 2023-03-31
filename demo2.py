from visa.entity.config_entity import DataIngestionConfig 
from visa.entity.artifact_entity import DataIngestionArtifact 
# from visa.config.configuration import Configuartion 
from visa.config.configuration import Configuration
import os,sys 
from visa.logger import logging 
from visa.pipeline.pipeline import Pipeline
from visa.exception import CustomException 

def main():
    try: 
        pipeline = Pipeline() 
        pipeline.run_pipeline() 
    except Exception as e:
        logging.error(f"{e}") 
        print(e) 
        
if __name__=='__main__':
    main()  