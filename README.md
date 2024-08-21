Designed and implemented a comprehensive data engineering solution leveraging Azure Cloud technologies. Key methods included:
  +	Architecture Design: Utilized Azure Data Factory (ADF), Azure Data Lake Gen2, Azure Blob Storage, Azure SQL Database, Azure Databricks, and Azure HDInsight.
  +	Data Integration: Configured ADF pipelines for seamless data integration from HTTP clients and storage solutions, utilizing control flow activities and metadata-driven pipelines.
  +	Data Transformation: Developed and executed data transformation logic with ADF Mapping Data Flows and Databricks notebooks.
  +	Advanced Analytics: Monitored and analysed pipeline performance using Azure Monitor and Log Analytics, creating alerts and visualizations.
  +	CI/CD Implementation: Set up Azure DevOps for continuous integration and deployment, streamlining the release process for ADF artefacts. 
# Azure Services Used in this Project. 

<img width="500" alt="services_used" src="https://github.com/user-attachments/assets/a153d522-9861-47c7-a903-62bd29af73c8">

# Project Architecture
Here is the overall project architecture.

<img width="527" alt="project_architecture" src="https://github.com/user-attachments/assets/33f0d385-e970-4bce-8fba-1b8fb1f34af6">

Below the Architecture Diagram.

<img width="529" alt="architecture_diagram" src="https://github.com/user-attachments/assets/cf396379-1d57-4e25-9e9b-3eb9715fbedd">

# Environmental Setup
To do this project, i have created 
  - Azure Subscription (free Azure Subscription)
  - Azure Data Factory
  - Azure Blob Storage
  - Azure Data Lake Gen 2
  - Azure SQL Database
  - Azure Databricks Cluster
  - Azure HDInsight Cluster

# Data ingestion from Azure Blob Storage to Azure DataLake Storage.
Here the idea is to ingest the data which are uploaded in the Azure Blob Storage to the Azure DataLake Storage using the Azure Data Factory Pipeline.
In order to do that, the requirement is given below.

<img width="530" alt="blob_to_datalake" src="https://github.com/user-attachments/assets/fc08b16b-d043-4a20-988e-0c0183103a25">

Requirements for doing this copy activity in ADF

  - Source --> Azure Blob Stotrage
  - Destination or Sink --> Azure Datalake Storage
  - Source Dataset
  - Linked Service for Source Dataset
  - Sink Dataset
  - Linked Service for Sink Dataset
  - Copy Activity from ADF
  - and Pipeline to include all these components.

Initially i tested the Data Pipeline by ingesting one file from Azure Blob Storage to Azure Data lake Storage by Copy Activity.
The Real World Problems i tried to implement in the Pipelines.

  - Applied Copy Data to Collect the file from Blob Storage to Data Lake Storage.
  - Validation Activity - Check if the File is Present in the Location (Source).
  - Get Metadata Activity - This will get the metadata of the file that is to ingested.
  - If Condition Activity - This is associated with the Get Metadata Output, if the get metadata output (column count is matching, the it will trigger the Copy Data Operation.)
  - From the Metadata Activity, it is possible to collect the data points like Column Count, File Size etc.
  - So in the If Condition, the column check will happen, two option is when true and false
  - When the Column Count Matches, the Copy Data Operation will be executed in the Pipeline.
  - After that the File in the Blob Storage which ingested will be deleted by a Delete Activity.
  - Implemented trigger to the Pipelines so that the Pipeline will run by Uploading the population file to the Source Blob Storage.

<img width="953" alt="pipeline1" src="https://github.com/user-attachments/assets/830eefd1-883a-4030-bfca-92c77d4cd22a">

# Data ingestion from HTTP to Azure DataLake Storage.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/cad265d7-a005-4750-b04d-b3facc1c32ca">

Files/Data to be Ingested from HTTP (ECDC Website/Github Page) to Azure Data lake Storage.
 1. Covid 19 - New Cases and Death by Country
 2. Covid 19 - Hospital Admissions and ICU Cases
 3. Covid 19 - Testing Numbers
 4. Covid 19 - Country Response

To develop a Pipeline for Ingesting Data from HTTP to Azure Data Lake required different components as shown in the figure.
 - Linked Service to Collect Data from HTTP
 - Dataset to Collect the Data from HTTP
 - Linked Service to Upldoad the Data to Azure Data Lake
 - Dataset to Upload Data to the Azure Data Lake
 - Copy Activity
 - Pipeline

+ The Pipeline is created to collect 4 files from ECDC Website. This is a Metadata Driven Pipeline.
+ The links to collect the Files are given below in this link which is the lookup file (.json file) : https://github.com/AMEERKOTTA/Project-Data-Engineering-Solution-Using-Azure-Cloud/blob/main/ECDC%20Data/ecdc_file_list.json
+ I have collected the links to get the BaseURL, RelativeURL and given the Fiilename to Save the FIles in Azure DataLake Storage.
+ The Pipeline is Automated by a Scheduled Trigger which will run every 15 minutes.
+ In that case it is possible to get the updated data for every 15 Minutes.

<img width="958" alt="image" src="https://github.com/user-attachments/assets/388bfdca-6d6b-47da-bbd3-1c2bc2a0ec37">

Triggers and Pipeline Runs

<img width="953" alt="image" src="https://github.com/user-attachments/assets/a27694cc-6ad3-4d43-b75e-700da53b5a35">

<img width="952" alt="image" src="https://github.com/user-attachments/assets/10bc957c-6755-4338-b990-a26035942e96">

# Cases and Deaths Data Transformation
In this task i have transformed the cases and deaths csv file using Azure Data Factory.
