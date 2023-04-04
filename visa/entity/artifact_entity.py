from collections import namedtuple 

DataIngestionArtifact = namedtuple('DataIngestionArtifact',['train_file_path','test_file_path','is_ingested','message']) 

#For Data Validation
DataValidationArtifact = namedtuple("DataValidationArtifact",["schema_file_path","is_validated","message"])

#DATA TRANSFORMATION 
DataTransformationArtifact = namedtuple("DataTransformationArtifact",['is_transformed','message','transformed_train_file_path',
                                                                      'transformed_test_file_path','preprocessed_object_file_path'])

