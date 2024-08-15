## move the uploaded file from blob storage to datalake storage

import os
from config import *
from azure.storage.blob import BlobServiceClient
from azure.storage.filedatalake import DataLakeServiceClient

# Azure Blob Storage connection details
blob_storage_connection_string = blob_storage_connection_string
blob_container_name = container_name

# Azure Data Lake Storage connection details
adls_connection_string = adls_connection_string
adls_filesystem_name = adls_filesystem_name

# Initialize Blob Service Client
blob_service_client = BlobServiceClient.from_connection_string(blob_storage_connection_string)
blob_container_client = blob_service_client.get_container_client(blob_container_name)
print("Blob Service Client initialization Completed")

# Initialize ADLS Service Client
adls_service_client = DataLakeServiceClient.from_connection_string(adls_connection_string)
adls_filesystem_client = adls_service_client.get_file_system_client(adls_filesystem_name)
print("DataLake Service Client initialization Completed")

def move_blob_to_adls(blob_name):
    try:
        # Download the blob from Blob Storage
        blob_client = blob_container_client.get_blob_client(blob_name)
        download_stream = blob_client.download_blob()
        
        # Upload to ADLS Gen2
        adls_file_client = adls_filesystem_client.get_file_client(blob_name)
        adls_file_client.upload_data(download_stream.readall(), overwrite=True)
        print(f"Successfully moved {blob_name} from Blob Storage to ADLS Gen2")
        
    except Exception as e:
        print(f"Failed to move {blob_name}: {str(e)}")

def delete_blob(blob_name):
    try:
        blob_client = blob_container_client.get_blob_client(blob_name)
        blob_client.delete_blob()
        print(f"Successfully deleted {blob_name} from Blob Storage")
        
    except Exception as e:
        print(f"Failed to delete {blob_name}: {str(e)}")

# List of files to move
files = [
    "testing_by_week_country.csv",
    "hospital_and_icu_admission_rates.csv",
    "new_cases_and_deaths.csv",
    "age_specific_new_cases.csv"
]

# Move each file from Blob Storage to ADLS Gen2
for file in files:
    move_blob_to_adls(file)
    delete_blob(file)

    