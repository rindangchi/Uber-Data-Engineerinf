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
3. Store data in the google cloud storage
4. ETL using MAGE. AI
5. xxx

## Detailed Steps
### 1. Create Data Model
The first step is to create data model, data modelling is a process to organize elements of the data and standarize how they relates each other. 
In the data model it will contain fact table and dimensional tables. Fact table is table containing metrics or quantitative measure that will be used for analysis, for example amount, tax_charge, transaction etc. It will contain foreign key comes from dimensional tables. In the other hand dimensional table will contain attributes that will be analyzed, columns in the dimensional table wil not change frequently, for example location, product name, etc. Dimensional tables will contain primary key that linked to fact table. Columns in these tables can be used for grouping & filtering. 
Below is the data table that I created. I created this data model using lucid app. (https://lucid.app/)

<br>


![Uber Data Model (4)](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/48867305-6fd4-4624-8e33-5625bd869fd1)


### 2. Convert the flat data model into the real data model using python 
The next step is to convert the flat data model that we have created in lucid.app into the real fact and dimension table. In this step we will use python programming in jupyter. In this step we will do cleaning & transformation, which in this step we will first cleaning the data and next we will transform the data into fact table and dimensional table that we have designed before in the data model.

#### 2.1. Data cleaning Process
The data cleaning process is described below. 
<br>
- First, make sure that all data is in the correct data type
Read the uber data which is in csv file:

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/d9a874d0-3177-4314-b69b-91bd57819eff)

Check if all data is in the correct data type or not. 

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/adde0c1f-d9c3-4add-b6ca-9294400bd2d8)


The date columns do not have correct data types, so need to convert the data type first
![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/8c457641-c95f-4c50-8fb3-d42277da220e)

Then re-check the data type again

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/835b213c-fa81-438f-8558-ef00a8679a26)


- Second, drop the duplicate values in the dataset

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/b1b71891-6bb0-4e26-983f-0a4e0688c91c)


#### 2.2. Data Transformation Process
Next we will create the fact table and the dimensions table.

- Datetime dimension table

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/eebe500a-4bb7-49c5-a6d7-20a3238522a4)

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/e23e5ad0-db08-47fc-b778-d35b9c9d4d81)

- Passenger count dimension table

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/fc45dff6-e409-4491-9e06-18879bc2dc28)

- Trip distance dimension table

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/d42e9248-1bdc-4b40-af06-743d6aeee453)

- Rate dimension table

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/678b4714-bda1-4489-9c08-08ea01c87b4b)

- pick up location and drop off location dimension table

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/b9b5d363-3a0a-423b-8554-341d09709e9f)

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/926536ec-1e36-4b43-aea8-c2844a3ed511)

- Payment type dimension table
  
![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/050bfa60-5838-4b3f-adb7-f7ffb860e7a0)

- Fact Table

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/58792366-2f09-4a98-b45b-2d3acbab0ef4)

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/11f6aa9b-49e8-4392-813f-7d91733a75b0)


### 3. Store Data in to Google Cloud Storage
The next step we will store our csv data into google cloud storage

####3.1. Create a new project
First we will create a new project in the google cloud.
1. Go to google cloud console : https://console.cloud.google.com/ . Then Create new project.

   ![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/841e2167-5b2b-480f-a080-a45dc92cde29)

   After that put the project name

   ![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/44030436-38d2-43fc-b7cb-3713065a7204)

   Here i created project named Uber Data Engineering

2. Next go to Cloud Storage, the place where we will store our data. You will find the Cloud Storage option in the left side of the site.
   
   ![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/d0538feb-4db5-4583-ad41-0da5dc9c5bd7)

   Once you are in the cloud storage section, then create a new bucket, by pressing the create button. Here I already create a bucket listed here. 

   ![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/192bc416-905e-4848-936b-16194189c96d)

   After a bucket is created, next step is to upload the csv file to the bucket.
  
   ![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/844182b1-6be1-4e29-9e6d-75c5d15ca03b)

   After uploading the csv file, we need to make the file public, so we can access it.
   To make it public, first make sure that you change the permission ninto fine grained.

   <img width="766" alt="image" src="https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/16773148-5f49-45b7-a282-a676b4cf9bae">

   Then change the access into public.

   ![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/f14a459d-f719-4bf6-9719-c65f83412020)

### 4. Create compute engine in the Google Cloud Project
Next we will create a compute engine to deploy the Mage. ai. The compute engine here is a virtual machine or computer that we can switch it on or off. 
In the left side choose compute engine like below:

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/6f76753a-46df-41d8-aa3f-66ad1c747e55)

Next create the new instance, here I already create a new instance as below:

![image](https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/581fe937-3a62-4571-a17b-50831630a27f)

After the instance is created we can launch the instance by just clicking the SSH in the right side. 
It will open up a new pop up, then in this pop up we will install some required setting and libraries.

<img width="653" alt="image" src="https://github.com/rindangchi/Uber-Data-Engineering/assets/10241058/375285d3-5430-47aa-b8bd-89b6287217ba">

Install the below setting and libraries in the virtual machine

```
# Install Python and pip 
sudo apt-get update

sudo apt-get install python3-distutils

sudo apt-get install python3-apt

sudo apt-get install wget

wget https://bootstrap.pypa.io/get-pip.py

sudo python3 get-pip.py

```

Next is to install MAge 

```
# Install Mage
sudo pip3 install mage-ai
```

Then create a new project by putting below code

```
mage start <project name>
```

Then a port will be appear. 
In a new browser tab put the public ip address then following by port number. like below example:
```
http://34.142.208.76:6789/
```

   
   
