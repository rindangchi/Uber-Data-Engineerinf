# Uber-Data-Engineering
Uber Data Engineering Project

## Introduction
This project is to do data engineering process from scratch using Uber Dataset. And then next will do data analysis on this. 
This project is following tutorial provided by Darshill Palmar from this youtube video: https://www.youtube.com/watch?v=WpQECq5Hx9g&t=921s

## Architecture
<img width="514" alt="image" src="https://github.com/rindangchi/Uber-Data-Engineerinf/assets/10241058/88dd3970-dc0f-4458-a719-a50e7eaf317a">

## Tools
Tools used for this project is described below: <br>
Programming Language : Python <br>
Google Cloud Platform : Google Storage, Compute Instance, Big Query, Looker Studio <br>
Modern Data Pipeline : https://www.mage.ai/ <br>

## Data Set
Dataset used for this project is Uber data set provided by the TLC Trip record data. This dataset contains some information such as pick up and drop-off locatios, trip fare, payment types etc. <br>
You can download the dataset here: https://github.com/rindangchi/Uber-Data-Engineerinf/blob/main/uber_data.csv <br>
More information about the dataset can be found on this website: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page <br>
Below is the explanation about each fields on the dataset: <br>

| Fields  | Description   |
| ------------- | ------------- |
| VendorID |  A code indicating the TPEP provider that provided the record. (1= Creative Mobile Technologies, LLC; 2= VeriFone Inc.) |
|tpep_pickup_datetime|The date and time when the meter was engaged. |
|tpep_dropoff_datetime |The date and time when the meter was disengaged. |
|Passenger_count |The number of passengers in the vehicle. |
|Trip_distance |The elapsed trip distance in miles reported by the taximeter|
|PULocationID|TLC Taxi Zone in which the taximeter was engaged|
|DOLocationID|TLC Taxi Zone in which the taximeter was disengaged|
|RateCodeID|The final rate code in effect at the end of the trip. (1= Standard rate, 2=JFK, 3=Newark, 4=Nassau or Westchester, 5=Negotiated fare, 6=Group ride|
|Store_and_fwd_flag|This flag indicates whether the trip record was held in vehiclememory before sending to the vendor, aka “store and forward,”because the vehicle did not have a connection to the server. (Y= store and forward trip, N= not a store and forward trip)|
|Payment_type |A numeric code signifying how the passenger paid for the trip. (1= Credit card, 2= Cash, 3= No charge, 4= Dispute, 5= Unknown, 6= Voided trip|
|Fare_amount|The time-and-distance fare calculated by the meter.|
|Extra |Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges.|
|MTA_tax |$0.50 MTA tax that is automatically triggered based on the metered rate in use.|
|Improvement_surcharge |$0.30 improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015.|
|Tip_amount |Tip amount – This field is automatically populated for credit card tips. Cash tips are not included.|
|Tolls_amount|Total amount of all tolls paid in trip. |
|Total_amount|The total amount charged to passengers. Does not include cash tips.|

## Steps
1. Extract the dataset and create data model that contains fact table and dimensional table
2. Convert the flat data model into the real data model using python 
3. xxx
4. xxx

## Detailed Steps
### 1. Create Data Model
The first step is to create data model, data modelling is a process to organize elements of the data and standarize how they relates each other. 
In the data model it will contain fact table and dimensional tables. Fact table is table containing metrics or quantitative measure that will be used for analysis, for example amount, tax_charge, transaction etc. It will contain foreign key comes from dimensional tables. In the other hand dimensional table will contain attributes that will be analyzed, columns in the dimensional table wil not change frequently, for example location, product name, etc. Dimensional tables will contain primary key that linked to fact table. Columns in these tables can be used for grouping & filtering. 
Below is the data table that I created. I created this data model using lucid app. (https://lucid.app/)

<br>


![Uber Data Model (4)](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/48867305-6fd4-4624-8e33-5625bd869fd1)


### 2. Data Cleaning & Transformation : Convert the flat data model into the real data model using python 
The next step is to convert the flat data model that we have created in lucid.app into the real fact and dimension table. In this step we will use python programming in jupyter. This steps is also called the cleaning & transformation steps, which in this step we will first cleaning the data and next we will transfor the data into fact table and dimensional table that we have designed before in the data model.

#### 2.1. Data cleaning Process
The data cleaning process is described below. 
<br>
- First, read the uber data which is in csv file:

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/7340ca9a-1f0a-4599-8a99-aa936abf9a63)

- Second, we need to check if all data is in the correct data type or not. 

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/327d509b-8f57-45e3-b10b-d535a5516454)

The date columns do not have correct data types, so need to convert the data type first
![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/8c457641-c95f-4c50-8fb3-d42277da220e)

Then re-check the data type again

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/835b213c-fa81-438f-8558-ef00a8679a26)





