import os
import requests

## download the files from ECDC Website
def download_file(url, local_filename):
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {local_filename}")


## give the url and filename details
files = [("https://opendata.ecdc.europa.eu/covid19/testing/csv/data.csv", "testing_by_week_country.csv"),
        ("https://opendata.ecdc.europa.eu/covid19/hospitalicuadmissionrates/csv/data.csv", "hospital_and_icu_admission_rates.csv"),
        ("https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv/data.csv", "new_cases_and_deaths.csv"),
        ("https://opendata.ecdc.europa.eu/covid19/agecasesnational/csv/data.csv", "age_specific_new_cases.csv")]

for url, filename in files:
    download_file(url, filename)

