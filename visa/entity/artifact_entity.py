from collections import namedtuple 

DataIngestionArtifact = namedtuple('DataIngestionArtifact',['train_file_path','test_file_path','is_ingested','message']) 

#For Data Validation
DataValidationArtifact = namedtuple("DataValidationArtifact",["schema_file_path","is_validated","message"])

#DATA TRANSFORMATION 
DataTransformationArtifact = namedtuple("DataTransformationArtifact",['is_transformed','message','transformed_train_file_path',
                                                                      'transformed_test_file_path','preprocessed_object_file_path'])

#Model Traniner 
ModelTrainerArtifact = namedtuple("ModelTrainerArtifact", ["is_trained", "message", "trained_model_file_path",
                                                           "train_f1", "test_f1", "train_accuracy", "test_accuracy",
                                                           "model_accuracy"]) 

# Model Evaluation 
ModelEvaluationArtifact = namedtuple("ModelEvaluationArtifact",["is_model_accepted","evaluated_model_path"]) 
