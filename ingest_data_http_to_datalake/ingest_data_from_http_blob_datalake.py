## download the data from ecdc website
## upload the data to blob storage
## move the data from blob to data lake
## and delete the files from directory and blob after the movement.

import os
import logging
import requests
from config import *
from azure.storage.blob import BlobServiceClient
from azure.storage.filedatalake import DataLakeServiceClient

## Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration for Azure services
BLOB_STORAGE_CONNECTION_STRING = blob_storage_connection_string
BLOB_CONTAINER_NAME = container_name
ADLS_CONNECTION_STRING = adls_connection_string
ADLS_FILESYSTEM_NAME = adls_filesystem_name


def download_file(url, local_filename):
    """Download file from a URL to a local file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(local_filename, 'wb') as file:
            file.write(response.content)
        logger.info(f"Downloaded {local_filename}")
    except requests.RequestException as e:
        logger.error(f"Failed to download {url}: {str(e)}")
        raise

def upload_to_blob_storage(local_file_path, blob_name):
    """Upload a file to Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_STORAGE_CONNECTION_STRING)
        blob_container_client = blob_service_client.get_container_client(BLOB_CONTAINER_NAME)
        blob_client = blob_container_client.get_blob_client(blob_name)
        with open(local_file_path, "rb") as file:
            blob_client.upload_blob(file, overwrite=True)
        logger.info(f"Uploaded {blob_name} to Blob Storage")
    except Exception as e:
        logger.error(f"Failed to upload {local_file_path} to Blob Storage: {str(e)}")
        raise

def move_blob_to_adls(blob_name):
    """Move a blob from Blob Storage to Azure Data Lake Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_STORAGE_CONNECTION_STRING)
        blob_container_client = blob_service_client.get_container_client(BLOB_CONTAINER_NAME)
        adls_service_client = DataLakeServiceClient.from_connection_string(ADLS_CONNECTION_STRING)
        adls_filesystem_client = adls_service_client.get_file_system_client(ADLS_FILESYSTEM_NAME)

        blob_client = blob_container_client.get_blob_client(blob_name)
        download_stream = blob_client.download_blob()
        
        adls_file_client = adls_filesystem_client.get_file_client(blob_name)
        adls_file_client.upload_data(download_stream.readall(), overwrite=True)
        
        logger.info(f"Moved {blob_name} from Blob Storage to ADLS Gen2")
    except Exception as e:
        logger.error(f"Failed to move {blob_name} to ADLS Gen2: {str(e)}")
        raise

def delete_local_file(local_file_path):
    """Delete a local file."""
    try:
        if os.path.exists(local_file_path):
            os.remove(local_file_path)
            logger.info(f"Deleted {local_file_path} from local system")
        else:
            logger.warning(f"{local_file_path} does not exist")
    except OSError as e:
        logger.error(f"Error deleting {local_file_path}: {str(e)}")
        raise

def delete_blob(blob_name):
    """Delete a blob from Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_STORAGE_CONNECTION_STRING)
        blob_container_client = blob_service_client.get_container_client(BLOB_CONTAINER_NAME)
        blob_client = blob_container_client.get_blob_client(blob_name)
        blob_client.delete_blob()
        logger.info(f"Deleted {blob_name} from Blob Storage")
    except Exception as e:
        logger.error(f"Failed to delete {blob_name} from Blob Storage: {str(e)}")
        raise



def main():
    """Main function to orchestrate the data engineering tasks."""
    for url, local_filename in FILES:
        # Download files from ECDC
        download_file(url, local_filename)

        # Upload to Azure Blob Storage
        upload_to_blob_storage(local_filename, local_filename)

        # Move files from Blob Storage to ADLS Gen2
        move_blob_to_adls(local_filename)

        # Delete local file after upload and move
        delete_local_file(local_filename)

        # Delete from Blob Storage after moving to ADLS
        delete_blob(local_filename)
        

if __name__ == "__main__":
    main()



