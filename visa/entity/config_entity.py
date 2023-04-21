from collections import namedtuple

DataIngestionConfig = namedtuple('DataIngestionConfig',['dataset_download_url','raw_data_dir','ingested_train_dir','ingested_test_dir'])

# after that we need to define above variable in constant from config.yaml

TrainingPipelineConfig = namedtuple('TrainingPipelineConfig',['artifact_dir']) 

#Data Validation 
DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

# DATA TRANSFORMATION 
DataTransformationConfig = namedtuple("DataTransformationConfig",["transformed_train_dir","transformed_test_dir","preprocessing_object_file_path"])

# Model Trainer 
ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy","model_config_file_path"])

#Model Evaluation 
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"]) 

#Model Pusher 
# ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])

