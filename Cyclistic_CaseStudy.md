![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/bf37abee-0da5-4ea3-91a3-2de542752fde)## About this case study

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/1d6770b4-dc32-4ba8-a17f-c7317b62950c)

*Photo obtained from https://www.wallpaperflare.com/orange-bicycle-lot-parked-during-daytime-bicycles-bike-sharing-wallpaper-wmdxp*

In this Case Study, I will assume the position of a Junior Data Analyst at a fictional bike-share company in Chicago called Cyclistic. The company renders its services to two types of customers:

* Casual Riders - Customers who avail single single-ride or full-day passes
* Annual Members - Customers who purchased an annual membership
  
The stakeholders of this company believe that maximizing the number of annual members would define the company's future success since annual members are much more profitable than casual riders. The company would like to gather insights on how annual and casual members use Cyclistic differently to craft a data-driven plan to convert casual riders to annual members which would be my task as a part of their analytics team.

## Ask
The business problem we're trying to solve here is how to convince casual members into annual members. Finding the difference between a casual to an annual member can possibly shed light on factors why they chose a specific type of membership. Considering these statements, the following business task is formulated:

* By differentiating and identifying trends and patterns in how casual riders and annual members use Cyclistic, a series of recommendations will be crafted to guide a data-driven marketing strategy to help convert casual riders into Cyclistic members.


The key stakeholders of this case study are the following:
* Lily Moreno - The director of marketing and my manager. Responsible for the development of campaigns and initiatives to promote the bike-share program.
* Cyclistic executive team - The executive team who will verdict the approval of the proposed marketing program.
* Cyclistic marketing analytics team - Primarily responsible for collecting, analyzing, and reporting and analyzing data to guide Cyclistic marketing strategy.

## Prepare

The data used in this case study were stored in an Amazon AWS cloud database, made available by Motivate International Inc which can be accessed through this link: [https://divvy-tripdata.s3.amazonaws.com/index.html]. The datasets were compressed into zip files, each file sorted in two ways, either per month or per quarter. The zip files organized per month have their file name consisting of the year and the month of each dataset followed by -divvy-tripdata. This will be the dataset chosen for analysis and the latest data, which is from July 2022 to July 2023 will be used.

### Assessing the credibility of the data
To assess the credibility of the chosen data, we'll examine it closely using the "ROCCC" framework, as follows:
* ***Reliable*** - The chosen data is publicly available and has a data license agreement. The dataset comes from a good source proving its fit for use. 
* ***Original*** - The dataset was from a third-party source and upon looking at the source, its originality is verified as it is owned by the city of Chicago and made available to the public.
* ***Comprehensive*** - Our problem at hand aims to find the difference between each type of user in the bike-sharing company. The dataset provides comprehensive information about the users of a bike-sharing company along with the type of membership of each user/
* ***Current*** - The most recent dataset chosen includes this year's and last year's data which shows its relevance and up-to-date.  
* ***Cited*** - Examining the data license agreement, the data used is well-cited.

## Process
### Data Wrangling
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

 To prepare the data for analysis, all 12 files should be combined into a single CSV file. After all the data were put into a single directory, the code below was executed on the same working directory.
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
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/42578ee6-03a1-4bca-8ba1-39c960095a12)

### Data Cleaning
Clean data ensures an accurate analysis. Data cleaning is then the next step in processing the data since the dataset used is not yet clean. First duplicate entries must be removed as this could skew our result. For this, ```the duplicated().sum()``` function is used.

```
merged_df.duplicated().sum()
```

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/14948fd3-e1af-43b4-bcd9-1b61a9205ac7)


The function returned 0 which means there are no duplicate entries in our data. Next, we'll ensure the consistency of the attributes. For this, the ```unique()``` function will be used. This also allows the checking of misspelled entries. The relevant attributes that needs to be checked are the ```rideable_type```, ```start_station_name```, ```end_station_name```, and ```member_casual```  columns.

```
merged_df['rideable_type'].unique()
```

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/36bb2b7f-8ccf-4d07-885c-f11502881104)

```
merged_df['start_station_name'].unique()
```

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/b16d5e44-f615-4f15-9d8e-a3cb0aae9e64)

```
merged_df['end_station_name'].unique()
```
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/a0827454-0c5c-4580-8d14-21f2b7c9c475)

```
merged_df['member_casual'].unique()
```
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/9d61b376-08c8-46bc-818c-db1b8b4a28c0)

The returned values are distinct showing that there are no misspelled entries. To look into the consistency of the attributes, the ``` info() ``` function is used.

```
merged_df.info()
````
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/ddc9cd46-fb02-4f06-86fc-e408cd0fc332)

The rest of the data types of the attributes seem correct, except for the ``` started_at ``` and ``` ended_at ``` columns shown as ``` object ``` data type but should be ``` datetime64 ```. To clean this, the ``` astype() ``` function is used.

``` 
merged_df['started_at'] = merged_df['started_at'].astype('datetime64')
merged_df['ended_at'] = merged_df['started_at'].astype('datetime64')
merged_df.info()
```
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/14170178-d3e8-4218-8970-bb6f988a8b5f)

As found earlier in the data wrangling stage, there are null values. To look into the null values deeper, we use the ``` isnull() ``` function.
```
merged_df.isnull().sum()
```
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/2ab932b1-ed75-47ae-85b8-02c3f183da3c)

The columns, ``` start_station_name ```, ``` end_station_name ``` , ``` start_station_id ```, ``` end_station_id ``` has a lot of null values. However, these attributes aren't very useful in our analysis along with ``` start_lat ```, ``` start_lng ```, ``` end_lat ``` and ``` end_lng ```  so we will just drop them using the ``` drop() ``` function.

```
merged_df = merged_df.drop(['start_station_name', 'end_station_name', 'start_station_id', 'end_station_id', 'start_lat', 'start_lng' , 'end_lat' , 'end_lng'], axis = 1)
merged_df.head()
```

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/f2622f5a-5ea9-4571-88e6-8f5cb899b65e)

For our analysis, an important quantity we can use is the duration of a ride. This can be readily derived from the dataset, by subtracting the ``` ended_at ``` column from the ``` started_at ``` column and storing this to a new attribute/column we'll name as ``` ride_duration_seconds``` which is the duration of a ride in seconds.

```
merged_df['ride_duration'] = merged_df['ended_at'] - merged_df['started_at']         # a dummy attribute
merged_df['ride_duration_seconds'] = merged_df['ride_duration'].dt.total_seconds()   # converting to seconds for usefulness
merged_df = merged_df.drop(['ride_duration'], axis = 1)                              # dropping the dummy attribute
merged_df.head()
```

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/9d6b24fd-569d-4e09-ad86-c5c0a56ba8f9)


Also, it would be useful later if there is an attribute indicating the time of day when the ride started. This can be extracted from the ``` started_at ``` column by using the ``` .dt.weekday() ``` function, which assumes the weeks starts on Monday (0 = Monday, 6 = Sunday) 
```
merged_df['day_of_week'] = merged_df['started_at'].dt.dayofweek
merged_df.head()
```

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/18c31086-f2ca-43f5-a38d-cd506989860b)

## Analyze

The data is now relatively clean so an analysis of the dataset can now be taken. A descriptive analysis can give us an overview of the dataset, which can be taken using the ``` describe() ``` function.

```
merged_df.describe()
```
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/3506182b-e824-443d-bc27-0b89ab7bb49e)

As we can see, the ``` min ``` of the ``` data_duration_seconds``` is negative which indicates that there are negative values in that column. However, the duration should only be positive, so the entries with these negative values will be cleaned by using the ``` drop() ``` function.

```
merged_df = merged_df.drop(merged_df[merged_df['ride_duration_seconds'] < 0].index)
merged_df.describe()
```
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/18188229-908a-40e1-b4f1-92455400fc88)

### Importing the dataset into an SQL table
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
![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/d7ceaead-6e25-415f-b091-4fa7b45a884b)

A quick ``` SELECT ``` query verifies the success of importing the data as table in our SQL database.

```
SELECT * FROM cyclistic 
LIMIT 100;
```

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/caf981a9-0374-4aa7-8713-46b2483dad4c)


After importing our data into the ``` cyclistic ``` table we can now perform queries. In this section, all data visualizations were done in Tableau Public.

### Population of Casual Riders Vs. Annual Members

**Query**
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

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/b0968a88-959e-404c-958e-1403ed88a039)


**Visualization**

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/6c784b5a-26fe-4f2a-a58c-a8c748f32d7b)

**Findings**

* More than half of Cyclistic's customers purchased annual membership
* Almost 40% of Cyclistic's customers are casual riders 

### Ride Duration Statistics of Casual Riders and Annual Members**

**Query**

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

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/b09c9eb9-2410-4701-bcbb-68ae97629a3c)

**Visualization**

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/f091ddc5-5d36-4abc-9261-4489f9916ade)

**Findings**

* The total ride duration of casual riders is 47% more than the total ride duration of annual members.
* The maximum ride duration of casual riders is 32% more than the maximum ride duration of annual members.
* Both casual riders and annual members have a minimum of 0 minutes of ride duration.
* Casual riders have an average of 28 minutes of ride duration but a high standard deviation means that the ride duration of casual riders in general varies significantly from this value.
* Annual members have an average of 13 minutes of ride duration, and a low standard deviation shows that most of the annual members' ride duration is more or less close to this value.

### Bike Preferences of Casual Riders and Annual Members

**Query**

```
SELECT
    rideable_type AS bike_type,
    COUNT(CASE member_casual WHEN 'casual' THEN 1 ELSE null END) AS casual_riders,
    COUNT(CASE member_casual WHEN 'member' THEN 1 ELSE null END) AS annual_members
FROM 
    cyclistic
GROUP BY
    rideable_type;
```

**Data**

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/21ea56b9-5376-4367-a817-a5ab15ed4bc4)

**Visualization**

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/50886f13-45f0-4243-a5df-e669341573dd)

![image](https://github.com/Eoinmark/Python-Projects/assets/145372680/a32f50f8-d1ac-4285-9b8f-fb2b3cd33348)

**Findings**
* For casual riders, the most popular choice for bike type is the electric bike (57.01%) followed by classic bike (36.78%) and then by docked bike (6.21%)
* For annual members, the most popular choice for bike type is the electric bike (51.90%) and then followed by the classic bike (36.78%).
* Both types of customers chose electric bikes the most, and dock bikes the least.

### Casual Riders VS Annual Members Weekly Cyclistic Use

**Query**

```
SELECT
    day_of_week,
    COUNT(CASE member_casual WHEN 'casual' THEN 1 ELSE null END) AS casual_riders,
    COUNT(CASE member_casual WHEN 'member' THEN 1 ELSE null END) AS annual_members
FROM
    cyclistic
GROUP BY
    day_of_week
ORDER BY
    day_of_week;
```

**Data**

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/0cb3abe6-be9b-4c73-be26-ba5aad119ed7)

**Visualization**

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/0dd459d3-39e6-4771-a4a6-84e36fd0147b)

**Findings**
* For casual riders, the use of Cyclistic is almost constant at the beginning of the week and then would rise towards the latter part of the week, peaking at Saturday and would gradually fall on Sunday until Monday of a new week.
* For annual members, the rise in the use of Cyclistic tends to be in the middle of the week and then would fall on the weekends.

### Casual Riders VS Annual Members Monthly Cyclistic Use

**Query**

```
SELECT
    MONTH(started_at) AS month_started, 
    YEAR(started_at) AS year_started,
    COUNT(CASE member_casual WHEN 'casual' THEN 1 ELSE null END) AS casual_riders,
    COUNT(CASE member_casual WHEN 'member' THEN 1 ELSE null END) AS annual_members
FROM
    cyclistic
GROUP BY
    year_started,
    month_started
ORDER BY
    year_started,
    month_started;
```

**Data**

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/b39ce222-499b-4223-91a3-74e8eb081f78)

For better access, the ```month_started``` is re-indexed to start from 1 (July 2022) to 13 (July 2023).

**Visualization**

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/a18c2a2e-035b-47c9-acb6-d40dc75758a0)

**Findings**
* Both casual riders and annual members show almost a similar trend in the use of Cyclistic over the course of a year.
* The peak month of Cyclistic use for both casual riders and annual members is in July which corresponds to summer month in Chicago [1].
* Cyclistic users, both for casual riders and annual members tend to rise in the middle of the year and then fall down at the start and end of the year.

## Share

The analysis of our data is summarized on a dashboard created using Tableau Public, and accessible through the link below:
https://public.tableau.com/authoring/Cyclistic_dashboard_16967675172600/Dashboard1#1

![image](https://github.com/Eoinmark/Data-Analytics-Portfolio/assets/145372680/a132b29b-ca0d-46d7-89d6-d6314950a5d1)

**Key Findings**
* More than half of Cyclistic's customers are annual members. The casual riders are only 40% of their total customers.
* Although there are more annual members, casual riders use Cyclistics more than the annual members as they have longer total ride duration and higher average ride duration.
* Casual riders tend to use Cyclistic more on the weekends probably to stroll around Chicago as a form of vacation.
* Annual members tend to use Cyclistic more on the weekdays, probably to commute to their workplaces.
* Both casual riders and annual members rise in number in the middle of the year which are the summer months (June to August) and decline at the end and start of the year, corresponding to the winter months (December to February).
* The most popular bike type for both casual riders and annual members is the electric bike, and the least popular type is the docked bike.

## Act
Upon the findings from the analysis of the data, here are my top three recommendations:
1. Offer a "weekend-only" annual membership which gives its members perks same with annual membership that are much more affordable but are only eligible on weekends starting Friday until Sunday.
2. Boost marketing during the summer months and offer a limited-time discount on annual membership from June to August to capitalize on the season when Cyclistic users are at their peak.
3. Offer a much cheaper version of the annual membership by limiting the type of bike available from 3 (electric bike, classic bike, and docked bike) to only 2 (electric bike and classic bike).

## Reference/s:
[1] https://weatherspark.com/y/14091/Average-Weather-in-Chicago-Illinois-United-States-Year-Round#:~:text=The%20warm%20season%20lasts%20for,low%20of%2070%C2%B0F.








