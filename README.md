# HDB Resale Price Dashboard

[Dashboard Link](https://public.tableau.com/app/profile/fizah.j/viz/HDBPrice_17375996452230/Dashboard1?publish=yes/)

[Dataset of HDB Resale Price](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view )

## Introduction
HDB, or the Housing Development Board, is a public housing initiative established by the Singapore Government on February 1, 1960, to address the housing crisis in Singapore. At that time, many people were living in unsanitary slums and overcrowded conditions.

HDB also offers a type of housing called Build-to-Order (BTO), where construction begins only if 65-75% of the flats are booked. The typical completion time for BTO projects is around three years or more.

HDB flats in the "Resale" category are those where the original owner has lived in the unit for at least five years. In prime areas, however, the owner must have lived in the flat for 10 years before it becomes eligible for resale.

To assist users interested in buying or selling their next property, I developed a dashboard that provides insights into how location impacts property values while analyzing current trends in the housing market. By reviewing historical data and market trends, users can gain valuable insights into pricing strategies that facilitate informed decision-making.

## Steps Followed in Exploratory Data Analysis



### Step 1: Authenticating with the OneMap API  
The project begins by connecting to the OneMap API, which provides geolocation data in Singapore. Authentication is essential to gain access to the API, achieved by sending login credentials to the API's authentication endpoint. Upon successful authentication, an access token is returned, which is required for making subsequent API requests.  

---

### Step 2: Testing the Connection  
After obtaining the access token, a test is performed to verify connectivity with the API. A sample query is sent to the reverse geocoding endpoint, which converts latitude and longitude coordinates into human-readable address details. Successful responses confirm that the integration with OneMap is functional.  

---

### Step 3: Data Cleaning and Preparation  
Using Jupyter Notebook, the dataset containing HDB resale transactions is cleaned and processed. The focus during this step is on grouping records by region and extracting unique addresses. These unique addresses are saved to a separate CSV file, which will later serve as the basis for geolocation retrieval.  

---

### Step 4: Fetching Geolocation Data from OneMap API  
With the unique addresses prepared, the next step is to retrieve geolocation details such as postal codes, latitude, and longitude. This is achieved by sending API requests for each address. A multithreaded approach is used to expedite the process, ensuring efficient handling of multiple requests simultaneously. The retrieved geolocation data is saved to a new CSV file for further use.  

---

### Step 5: Merging Geolocation Data with the Main Dataset  
The main dataset, containing HDB resale transactions, is merged with the geolocation data. The process involves matching addresses between the two datasets to append geolocation details to the resale records. Additionally, a region column is introduced to group transactions by location. This step ensures the dataset is enriched with spatial information, enabling more meaningful analysis.  
