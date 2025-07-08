
Zomato
  Created by:
       Ankesh Kumar
       Hiralal Kr. Mahto
Project: DATA ANALYSIS ON ZOMATO RESTAURANT AND CUSTOMER BEHAVIOR
Project Overview

We aim to address the following key problems

1. Which cuisines are the most popular → Count how often each cuisine appears and rank them.

2. Which cities have the highest-rated restaurants → Average ratings per city to identify top food destinations.

3. Does online delivery affect ratings → Compare average ratings for restaurants that do and don’t offer online delivery.

4. What is the distribution of price ranges among restaurants → Show how many restaurants fall into each price range (1 to 4).

5. Which restaurants have the most votes → Identify the top 10 most-reviewed restaurants by vote count.

6. What is the relationship between average cost and rating → Use a scatter plot to explore if expensive restaurants get better ratings.

7. Availability of online delivery and table booking → Compare average ratings of restaurants with and without table booking.

8. How many restaurants exist per city in India → Group by city in India and count the number of listings.

Imported Pandas with allias pd to manage and handle the files with data.


[ ]
import pandas as pd
import numpay as np
Mounting Drive to Google Colab with full access to the files.


[ ]
# google colab users

from google.colab import drive
drive.mount('/content/drive')

# /content/drive/MyDrive/Colab Notebooks/zomato.csv
Mounted at /content/drive
Added the dataset


[ ]
import pandas as pd

# Define the file path
file_path = "/content/drive/MyDrive/Dataset/zomato.csv"
Zomato csv.......

To show the data from the dataset


[ ]
# Read the CSV file into a DataFrame
zomato_df = pd.read_csv(file_path, encoding='latin1')

# Display the first few records
print("First 5 rows of the dataset:")
print(zomato_df.head())

# Display dataset information
print("\nDataset Information:")
zomato_df.info()
First 5 rows of the dataset:
   Restaurant ID         Restaurant Name  Country Code              City  \
0        6317637        Le Petit Souffle           162       Makati City   
1        6304287        Izakaya Kikufuji           162       Makati City   
2        6300002  Heat - Edsa Shangri-La           162  Mandaluyong City   
3        6318506                    Ooma           162  Mandaluyong City   
4        6314302             Sambo Kojin           162  Mandaluyong City   

                                             Address  \
0  Third Floor, Century City Mall, Kalayaan Avenu...   
1  Little Tokyo, 2277 Chino Roces Avenue, Legaspi...   
2  Edsa Shangri-La, 1 Garden Way, Ortigas, Mandal...   
3  Third Floor, Mega Fashion Hall, SM Megamall, O...   
4  Third Floor, Mega Atrium, SM Megamall, Ortigas...   

                                     Locality  \
0   Century City Mall, Poblacion, Makati City   
1  Little Tokyo, Legaspi Village, Makati City   
2  Edsa Shangri-La, Ortigas, Mandaluyong City   
3      SM Megamall, Ortigas, Mandaluyong City   
4      SM Megamall, Ortigas, Mandaluyong City   

                                    Locality Verbose   Longitude   Latitude  \
0  Century City Mall, Poblacion, Makati City, Mak...  121.027535  14.565443   
1  Little Tokyo, Legaspi Village, Makati City, Ma...  121.014101  14.553708   
2  Edsa Shangri-La, Ortigas, Mandaluyong City, Ma...  121.056831  14.581404   
3  SM Megamall, Ortigas, Mandaluyong City, Mandal...  121.056475  14.585318   
4  SM Megamall, Ortigas, Mandaluyong City, Mandal...  121.057508  14.584450   

                           Cuisines  ...          Currency Has Table booking  \
0        French, Japanese, Desserts  ...  Botswana Pula(P)               Yes   
1                          Japanese  ...  Botswana Pula(P)               Yes   
2  Seafood, Asian, Filipino, Indian  ...  Botswana Pula(P)               Yes   
3                   Japanese, Sushi  ...  Botswana Pula(P)                No   
4                  Japanese, Korean  ...  Botswana Pula(P)               Yes   

  Has Online delivery Is delivering now Switch to order menu Price range  \
0                  No                No                   No           3   
1                  No                No                   No           3   
2                  No                No                   No           4   
3                  No                No                   No           4   
4                  No                No                   No           4   

   Aggregate rating  Rating color Rating text Votes  
0               4.8    Dark Green   Excellent   314  
1               4.5    Dark Green   Excellent   591  
2               4.4         Green   Very Good   270  
3               4.9    Dark Green   Excellent   365  
4               4.8    Dark Green   Excellent   229  

[5 rows x 21 columns]

Dataset Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9551 entries, 0 to 9550
Data columns (total 21 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Restaurant ID         9551 non-null   int64  
 1   Restaurant Name       9551 non-null   object 
 2   Country Code          9551 non-null   int64  
 3   City                  9551 non-null   object 
 4   Address               9551 non-null   object 
 5   Locality              9551 non-null   object 
 6   Locality Verbose      9551 non-null   object 
 7   Longitude             9551 non-null   float64
 8   Latitude              9551 non-null   float64
 9   Cuisines              9542 non-null   object 
 10  Average Cost for two  9551 non-null   int64  
 11  Currency              9551 non-null   object 
 12  Has Table booking     9551 non-null   object 
 13  Has Online delivery   9551 non-null   object 
 14  Is delivering now     9551 non-null   object 
 15  Switch to order menu  9551 non-null   object 
 16  Price range           9551 non-null   int64  
 17  Aggregate rating      9551 non-null   float64
 18  Rating color          9551 non-null   object 
 19  Rating text           9551 non-null   object 
 20  Votes                 9551 non-null   int64  
dtypes: float64(3), int64(5), object(13)
memory usage: 1.5+ MB
Level 1: Data Understanding & Cleaning
The goal is to understand and clean the dataset before deeper analysis.

We focus on:

Data Overview (Structure, Columns, Data Types)

Checking for Missing Values

Detecting Duplicates

Handling Inconsistencies

To check number of rows and columns


[ ]
zomato_df.shape

To check features of the schemas available in the data


[ ]
zomato_df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9551 entries, 0 to 9550
Data columns (total 21 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Restaurant ID         9551 non-null   int64  
 1   Restaurant Name       9551 non-null   object 
 2   Country Code          9551 non-null   int64  
 3   City                  9551 non-null   object 
 4   Address               9551 non-null   object 
 5   Locality              9551 non-null   object 
 6   Locality Verbose      9551 non-null   object 
 7   Longitude             9551 non-null   float64
 8   Latitude              9551 non-null   float64
 9   Cuisines              9542 non-null   object 
 10  Average Cost for two  9551 non-null   int64  
 11  Currency              9551 non-null   object 
 12  Has Table booking     9551 non-null   object 
 13  Has Online delivery   9551 non-null   object 
 14  Is delivering now     9551 non-null   object 
 15  Switch to order menu  9551 non-null   object 
 16  Price range           9551 non-null   int64  
 17  Aggregate rating      9551 non-null   float64
 18  Rating color          9551 non-null   object 
 19  Rating text           9551 non-null   object 
 20  Votes                 9551 non-null   int64  
dtypes: float64(3), int64(5), object(13)
memory usage: 1.5+ MB
To check null values in True and False


[ ]
zomato_df.isnull()

To check the count of all the null values


[ ]
zomato_df.isnull().sum()

To check the column names(default top 5 values)


[ ]
zomato_df.head()

To check and drop if any duplicated rows in the dataset


[ ]
duplicated_rows=zomato_df.duplicated().sum()
print(duplicated_rows)
0
1. Most Popular Cuisines

[ ]
# Top 10 cuisines
import matplotlib.pyplot as plt
import seaborn as sns

top_cuisines = zomato_df['Cuisines'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette='Set2')
plt.title("Top 10 Most Popular Cuisines")
plt.xlabel("Number of Restaurants")


2. Top 10 Highest Rated Restaurants

[ ]
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/zomato.csv', encoding='latin1')

# Group by City and calculate the average rating, filtering out 0 ratings (optional)
city_avg_rating = df[df['Aggregate rating'] > 0].groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=city_avg_rating.values, y=city_avg_rating.index, palette='viridis')
plt.title("Top 10 Cities with Highest Average Restaurant Ratings")
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.xlim(0, 5)  # Ratings are between 0 and 5
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


3. Online Delivery vs Rating

[ ]
plt.figure(figsize=(8, 5))
sns.boxplot(x='Has Online delivery', y='Aggregate rating', data=df, palette='Set3')
plt.title("Online Delivery vs Aggregate Rating")
plt.xlabel("Has Online Delivery")
plt.ylabel("Rating")
plt.show()

4. Top 5 Budget-Friendly Restaurants (Price Range = 1 and Rating > 4.0)

[ ]
import matplotlib.pyplot as plt
import seaborn as sns

# Filter: Price range = 1 and rating > 4.0
budget_friendly = df[(df['Price range'] == 1) & (df['Aggregate rating'] > 4.0)]

# Sort by rating and select top 5
top_budget = budget_friendly.sort_values(by='Aggregate rating', ascending=False).head(5)

# Show data
print("💸 Top 5 Budget-Friendly Restaurants:\n")
print(top_budget[['Restaurant Name', 'City', 'Cuisines', 'Aggregate rating', 'Votes']])

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x='Aggregate rating', y='Restaurant Name', data=top_budget, palette='Purples')
plt.title("💸 Top 5 Budget-Friendly Restaurants")
plt.xlabel("Aggregate Rating")
plt.ylabel("Restaurant Name")
plt.xlim(4.0, 5.0)
plt.grid(axis='x', linestyle='--')
plt.show()

5. Top 10 Most Voted Restaurants:

[ ]
most_voted = df.sort_values(by='Votes', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Votes', y='Restaurant Name', data=most_voted, palette='Blues_r')
plt.title("📢 Top 10 Most Voted Restaurants")
plt.xlabel("Votes")
plt.ylabel("Restaurant Name")
plt.show()

6. Average cost vs aggregate rating

[ ]
plt.figure(figsize=(8, 5))
sns.boxplot(x='Price range', y='Aggregate rating', data=df, palette='coolwarm')
plt.title("Price Range vs Aggregate Rating")
plt.xlabel("Price Range (1=Cheap, 4=Expensive)")
plt.ylabel("Aggregate Rating")
plt.show()


7. Top 5 Restaurants Offering Online Delivery

[ ]
import matplotlib.pyplot as plt
import seaborn as sns

# Filter: Restaurants that offer online delivery
online_delivery = df[df['Has Online delivery'] == 'Yes']

# Sort by rating and select top 5
top_online_delivery = online_delivery.sort_values(by='Aggregate rating', ascending=False).head(5)

# Print data slice
print("🚚 Top 5 Restaurants Offering Online Delivery:\n")
print(top_online_delivery[['Restaurant Name', 'City', 'Cuisines', 'Aggregate rating', 'Votes']])

# Visualize
plt.figure(figsize=(10, 6))
sns.barplot(x='Aggregate rating', y='Restaurant Name', data=top_online_delivery, palette='YlGnBu')
plt.title("🚚 Top 5 Restaurants Offering Online Delivery")
plt.xlabel("Aggregate Rating")
plt.ylabel("Restaurant Name")
plt.xlim(4.0, 5.0)
plt.grid(axis='x', linestyle='--')
plt.show()

8. Restaurants per City in India

[ ]
# Top 10 cities with most restaurants
top_cities = df['City'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette='pastel')
plt.title("Top 10 Cities by Restaurant Count")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.show()

✅ 📄 Conclusion
1.The Zomato dataset reveals valuable insights into restaurant ratings, cuisines, and cost patterns across cities.

2.Popular cuisines include North Indian, Chinese, and Italian, reflecting diverse customer preferences.

3.Cities like New Delhi and Bangalore host the highest number of top-rated restaurants.

4.There is no strong correlation between cost and rating—great food isn't always expensive.

5.Features like table booking and location play a notable role in customer satisfaction and ratings.

Colab paid products - Cancel contracts here

