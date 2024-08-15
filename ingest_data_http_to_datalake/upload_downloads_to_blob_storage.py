## upload the files to blob storage
## and delete the downloaded files.

import os
from config import blob_storage_connection_string, container_name
from azure.storage.blob import BlobServiceClient

## get the azure blob storage 
blob_storage_connection_string = blob_storage_connection_string
container_name = container_name

## Initialize Blob Service Client
blob_service_client = BlobServiceClient.from_connection_string(blob_storage_connection_string)
container_client = blob_service_client.get_container_client(container_name)


## Function to upload a file to Blob Storage
def upload_to_blob_storage(local_file_path, blob_name):
    blob_client = container_client.get_blob_client(blob_name)
    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"Uploaded {blob_name} to Blob Storage")

## Function to delete the local file
def delete_local_file(local_file_path):
    if os.path.exists(local_file_path):
        os.remove(local_file_path)
        print(f"Deleted {local_file_path} from local system")
    else:
        print(f"{local_file_path} does not exist")


# List of files to upload and delete
files = [
    "testing_by_week_country.csv",
    "hospital_and_icu_admission_rates.csv",
    "new_cases_and_deaths.csv",
    "age_specific_new_cases.csv"
]

# Upload each file to Blob Storage and delete the local file
for file in files:
    upload_to_blob_storage(file, file)  # Use the same name for blob as the local file
    delete_local_file(file)