## About this case study
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/c0c97fa8-7952-4bfd-b25d-1ecd388e3a46)

*Photo obtained from https://www.wallpaperflare.com/orange-bicycle-lot-parked-during-daytime-bicycles-bike-sharing-wallpaper-wmdxp*

In this Case Study, I will assume the position of a Junior Data Analyst at a bike-share company in Chicago. The company renders its services to two types of customers:

* Casual Members - Customers who avail single single-ride or full-day passes
* Annual Members - Customers who purchased an annual membership
  
The stakeholders of this company believe that maximizing the number of annual members would define the company's future success. The company would like to gather insights on how annual and casual members use Cyclistic differently to craft a data-driven plan to convert casual riders to annual members which would be my task as a part of their analytics team.

## Ask
The business problem we're trying to solve here is how to convince casual members into annual members. Finding the difference between a casual to an annual member can possibly shed light on factors why they chose a specific type of membership. Considering these statements, the following business task is formulated:

"Through analyzing the difference between casual and annual members, the factors affecting their decision to commit to a certain type of membership would be identified and which would help in crafting a data-driven plan to convert more customers to avail the desired annual membership"

## Prepare

The data used in this case study were stored in an Amazon AWS cloud database, made available by Motivate International Inc which can be accessed through this link: [https://divvy-tripdata.s3.amazonaws.com/index.html]. The datasets were compressed into zip files, each file sorted in two ways, either per month or per quarter. The zip files organized per month have their file name consisting of the year and the month of each dataset followed by -divvy-tripdata. This will be the dataset chosen for analysis and the latest data which is from March 2022 to March 2023 will be used.

#### Assessing the credibility of the data
To assess the credibility of the chosen data, we'll examine it closely using the "ROCCC" framework, as follows:
* ***Reliable*** - The chosen data is publicly available and has a data license agreement. It is a suggested dataset by the Google Data Analytics course proving its fit for use. (from good source)
* ***Original*** - The dataset was from a third-party source and upon looking at the source, its originality is verified as it is owned by the city of Chicago and made available to the public.
* ***Comprehensive*** - Our problem at hand aims to find the difference between each type of user in the bike-sharing company. The dataset provides comprehensive information about the users of a bike-sharing company along with the type of membership of each user/
* ***Current*** - The most recent dataset chosen includes this year's and last year's data which shows its relevance and up-to-date.  
* ***Cited*** - Examining the data license agreement, the data used is well-cited.

## Process
#### Data Wrangling
The downloaded dataset is compressed into zipfiles. After extracting, the dataset is in CSV format having the same 13 attributes as given below:
* ride_id: Character data type, a unique identifier for each user
* rideable_type: Character data type, describes the type of bike used
* started_at: date-time data type, indicates the starting time a customer rented a bike
* ended_at: date-time data type, indicates the time a customer returned a rented bike
* start_station_name: Character data type, the location where the bike is rented
* start_station_id: Character data type, a unique identifier for a starting station
* end_station_name: Character data type, the location where the bike rented is returned
* end_station_id: Character data type, a unique identifier for an end station
* start_lat: Geographical data type, the latitude of a starting station's location
* start_lng: Geographical data type, the longitude of a starting station's location
* end_lat: Geographical data type, the latitude of an end station's location
* end_lng: Geographical data type, the longitude of an end station's location
* member_casual: Character data type, indicates the type of membership of a customer

 To prepare the data for analysis, all 12 files should be combined into a single CSV file. After all the dataset were put into a single directory, the code below were executed on the same working directory.
```
import os
import pandas as pd

merged_df = pd.DataFrame()  #create an empty dataframe

for file in os.listdir(os.getcwd()):  #populate the dataframe with the content of the csv files
    if file.endswith('.csv'):
        merged_df = merged_df.append(pd.read_csv(file))
    
merged_df.to_csv('Cyclistic_data.csv', index=False)
```
Python were used for this process, specfically through os library, to get the files and the pandas library to merge them into one. To verify if the merging is correct, the created dataframe was previewed using the ``` display() ``` function. Upon examination of the preview of the dataframe shown below, there seems to be no problem except for some null values which will be addressed on the next step which is data cleaning.
```
display(merged_df)
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/63e28495-8d2c-40cd-af46-6d68cd5146fa)

#### Data Cleaning
A clean data ensures an accurate analysis. Data cleaning is then the next step in processing the data since the dataset used in not yet clean. First duplicate entries must be removed as this could skew our result. For this, ```the duplicated().sum()``` function is used.

```
merged_df.duplicated().sum()
```

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/f2a9e7e5-db7b-4f87-8152-a45e8b18e72c)

The function returned 0 which means there are no duplicate entry in out data. Next we'll ensure that the consistency of the attributes. For this, the ```unique()``` function will be used. This also allows the checking of mispelled entries. The relevant attributes that needs to be checked are the ```rideable_type```, ```start_station_name```, ```end_station_name```, and ```member_casual```  columns.

```
merged_df['rideable_type'].unique()
```

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/bc55c19e-2c45-4db9-afac-444506d5e2e6)

```
merged_df['start_station_name'].unique()
```

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/54ec9fac-8238-4370-8ab7-4d78ee19d667)

```
merged_df['end_station_name'].unique()
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/6fe35e62-27e3-4e0b-8fdc-757bcde00293)


```
merged_df['member_casual'].unique()
```

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/9dc49a08-7cde-45f4-9139-dd52e9798197)



