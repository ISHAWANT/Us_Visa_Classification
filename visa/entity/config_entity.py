from collections import namedtuple

DataIngestionConfig: namedtuple('DataIngestionConfig',['dataset_download_url','raw_data_dir','ingested_train_dir','ingested_test_dir'])

# after that we need to define above variable in constant from config.yaml

# DataValidationConfig: namedtuple("DataValidationConfig",["schema_file_dir"]) 