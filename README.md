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

For this task i have 4 files, Collect the data from ECDC website and Upload the files to Azure Blob Storage and the Ingest those files to the Azure DataLake Storage.
