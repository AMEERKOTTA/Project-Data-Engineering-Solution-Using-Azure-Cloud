# Databricks notebook source
storage_account_name = "covid19datalakestore"
storage_account_key = "XN17iHYkCBD8OABpvRzb8ZwpZFZSmXycYmb7hcJ+DnTfo0g0T28tJ4KjCEGFzh/9idgQWn3+d+Gt+AStIQ39mA=="

spark.conf.set(f"fs.azure.account.key.{storage_account_name}.dfs.core.windows.net", storage_account_key)

## mount population-raw-files container
dbutils.fs.mount(
  source = f"wasbs://population-raw-files@{storage_account_name}.blob.core.windows.net/",
  mount_point = "/mnt/population_data",
  extra_configs = {f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": storage_account_key}
)

# COMMAND ----------

dbutils.fs.ls("/mnt/population_data")

# COMMAND ----------

df = spark.read.format("csv").option("header", "true").load("/mnt/population_data/population.csv")

# COMMAND ----------

df.show()

# COMMAND ----------

## mount the dim_country lookup container
dbutils.fs.mount(
  source = f"wasbs://lookup-country@{storage_account_name}.blob.core.windows.net/",
  mount_point = "/mnt/dim_country",
  extra_configs = {f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": storage_account_key}
)

## mount the dim_date container
dbutils.fs.mount(
  source = f"wasbs://lookup-dimdate@{storage_account_name}.blob.core.windows.net/",
  mount_point = "/mnt/dim_date",
  extra_configs = {f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net": storage_account_key}
)

# COMMAND ----------

dbutils.fs.ls("/mnt/dim_country")

# COMMAND ----------

df_country = spark.read.format("csv").option("header", "true").load("/mnt/dim_country/country_lookup.csv")

# COMMAND ----------

df_country.show()

# COMMAND ----------

dbutils.fs.ls("/mnt/dim_date")

# COMMAND ----------

df_date = spark.read.format("csv").option("header", "true").load("/mnt/dim_date/dim_date.csv")

# COMMAND ----------

df_date.show()

# COMMAND ----------


