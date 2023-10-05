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

 To prepare the data for analysis, all 12 files should be combined into a single CSV file. After all the dataset were put into a single directory, the code below was executed on the same working directory.
```
import os
import pandas as pd

merged_df = pd.DataFrame()  #create an empty dataframe

for file in os.listdir(os.getcwd()):  #populate the dataframe with the content of the csv files
    if file.endswith('.csv'):
        merged_df = merged_df.append(pd.read_csv(file))
    
merged_df.to_csv('Cyclistic_data.csv', index=False)
```
Python was used for this process, specifically through os library, to get the files and the pandas library to merge them into one. To verify if the merging is correct, the created data frame was previewed using the ``` display() ``` function. Upon examination of the preview of the data frame shown below, there seems to be no problem except for some null values which will be addressed on the next step which is data cleaning.
```
display(merged_df)
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/63e28495-8d2c-40cd-af46-6d68cd5146fa)

#### Data Cleaning
Clean data ensures an accurate analysis. Data cleaning is then the next step in processing the data since the dataset used in not yet clean. First duplicate entries must be removed as this could skew our result. For this, ```the duplicated().sum()``` function is used.

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

The returned values are distinct showing that there are no misspelled entries. To look into the consistency of the attributes, the ``` info() ``` function is used.

```
merged_df.info()
````
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/31c1d6e8-e3c1-4ff0-99f3-d8fa74cde087)

The rest of the data types of the attributes seem correct, except for the ``` started_at ``` and ``` ended_at ``` columns shown as ``` object ``` data type but should be ``` datetime64 ```. To clean this, the ``` astype() ``` function is used.

``` 
merged_df['started_at'] = merged_df['started_at'].astype('datetime64')
merged_df['ended_at'] = merged_df['started_at'].astype('datetime64')
merged_df.info()
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/0fd4d701-4254-43a9-ab04-1d76897d5f58)

As found earlier in the data wrangling stage, there are null values. To look into the null values deeper, we use the ``` isnull() ``` function.
```
merged_df.isnull().sum()
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/d9f1f2e8-bbc7-4abf-9eb6-349d6aec85c8)

The columns, ``` start_station_name ```, ``` end_station_name ``` , ``` start_station_id ```, ``` end_station_id ``` has a lot of null values. However, these attributes aren't very useful in our analysis along with ``` start_lat ```, ``` start_lng ```, ``` end_lat ``` and ``` end_lng ```  so we will just drop them using the ``` drop() ``` function.

```
merged_df = merged_df.drop(['start_station_name', 'end_station_name', 'start_station_id', 'end_station_id', 'start_lat', 'start_lng' , 'end_lat' , 'end_lng'], axis = 1)
merged_df.head()
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/6da4d304-4cba-4e6d-803f-a161508bdbf9)


For our analysis, an important quantity we can use is the duration of a ride. This can be readily derived from the dataset, by subtracting the ``` ended_at ``` column from the ``` started_at ``` column and storing this to a new attribute/column we'll name as ``` ride_duration_seconds``` which is the duration of a ride in seconds.

```
merged_df['ride_duration'] = merged_df['ended_at'] - merged_df['started_at']         # a dummy attribute
merged_df['ride_duration_seconds'] = merged_df['ride_duration'].dt.total_seconds()   # converting to seconds for usefulness
merged_df = merged_df.drop(['ride_duration'], axis = 1)                              # dropping the dummy attribute
merged_df.head()
```

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/32d48685-a39d-4e7c-83c8-942e98e86512)


Also, it would be useful later if there is an attribute indicating the time of day when the ride started. This can be extracted from the ``` started_at ``` column by using the ``` .dt.weekday() ``` function, which assumes the weeks starts on Monday (0 = Monday, 6 = Sunday) 
```
merged_df['day_of_week'] = merged_df['started_at'].dt.dayofweek
merged_df.head()
```

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/a8698ec8-e80c-4440-915a-dc559f7b6d44)


## Analyze

The data is now relatively clean so an analysis of the dataset can now be taken. A descriptive analysis can give us an overview of the dataset, which can be taken using the ``` describe() ``` function.

```
merged_df.describe()
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/b4d1da4e-cfba-4005-b8c6-9d53d4edc9d7)


As we can see, the ``` min ``` of the ``` data_duration_seconds``` is negative which indicates that there are negative values in that column. However, the duration should only be positive, so the entries with these negative values will be cleaned by using the ``` drop() ``` function.

```
merged_df = merged_df.drop(merged_df[merged_df['ride_duration_seconds'] < 0].index)
merged_df.describe()
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/f7978d25-8651-4091-ac25-22fb935bfe42)



#### Importing the dataset into an SQL table
Now that the data is thoroughly cleaned, a more in-depth analysis can be done using Excel, Sheets, or SQL. Since the dataset is too large for Excel or Sheets to handle, we will use SQL, specifically MySQL using POPSQL editor. But first, we export our pre-processed data as a CSV file

```
merged_df.to_csv('Cyclistic_data_cleanedd.csv', index=False)
```

To work with the data in SQL, we must first create a table with the same attributes as our data and then populate it with the values of our cleaned data.

```
CREATE TABLE cyclistic (
    ride_id VARCHAR(50) PRIMARY KEY,
    rideable_type VARCHAR(50),
    started_at DATETIME,
    ended_at DATETIME,  
    member_casual VARCHAR(50),
    ride_duration_seconds DOUBLE,
    day_of_week INT
);
```
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/81cee3d0-e99b-4c55-a6c2-ed7401c1b922)


```
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.1/Uploads/Cyclistic_data_cleanedd.csv" INTO TABLE Cyclistic FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

```

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/5c7f08ac-3dfc-4109-b99e-dc054e998803)

A quick ``` SELECT ``` query verifies the success of importing the data as table in our SQL database.

```
SELECT * FROM cyclistic 
LIMIT 100;
```

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/709de4e9-a804-4961-b5e5-379a426d3d1e)



#### Data Findings

After importing our data into the ``` cyclistic ``` table we can now perform queries, such as querying to know the population of the the casual members ``` casual ```, and annual members ``` member ```. 

```
SELECT 
    member_casual AS membership_type,
    COUNT(member_casual) AS total_members
FROM
    cyclistic
GROUP BY
    member_casual;
```
**Data**

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/c7efcaf6-9db6-4afc-b5e6-115292aeb987)

**Chart**

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/79dfdbe6-c2d6-482c-a311-785ce5364f20)

*insert tableau visualization here*

**Findings**
* More than half of Cyclistic's customers purchased annual membership
* Almost 40% of Cyclistic's customers are casual riders 

Next, we look into the ``` ride_duration ``` statistics of a casual rider vs. an annual member.

```
SELECT
    member_casual AS membership_type,
    SUM(ride_duration_seconds)/60 AS total_ride_duration_min,
    MAX(ride_duration_seconds)/60 AS max_ride_duration_min,
    MIN(ride_duration_seconds)/60 AS min_ride_duration_min,
    AVG(ride_duration_seconds)/60 AS avg_ride_druation_min,
    STDDEV(ride_duration_seconds)/60 AS stddev_ride_duration_min
FROM 
    cyclistic
GROUP BY
    member_casual;
```
**Data**
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/d9267c32-2cd8-4215-a25e-43e10e6018f0)

**Visualization**
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/48deda44-b2e1-4374-aa67-ac7de3a3eb2e) 
![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/51aae5b5-8d25-4565-a1ee-ec3aa03ef247)

**Findings**
* The total ride duration of casual riders is 47% more than the total ride duration of annual members.
* The maximum ride duration of casual riders is 32% more than the maximum ride duration of annual members.
* Both casual riders and annual members have a minimum of 0 minutes of ride duration.
* Casual riders have an average of 28 minutes of ride duration but a high standard deviation means that ride duration of the casual riders in general varies significantly from this value.
* Annual members have an average of 13 minutes, and a low standard deviation shows that most of the annual members' ride duration are more or less close to this value.







