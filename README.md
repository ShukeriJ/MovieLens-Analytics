<img width="340" height="100" alt="movielens" src="https://github.com/user-attachments/assets/c8b49e0c-81a5-4041-9a8a-66ef8bd46dea" />

# 🎬 MovieLens Analytics Pipeline

Apache Spark + Hadoop HDFS + Cassandra Analytics Project

![Spark](https://img.shields.io/badge/Apache-Spark-orange)
![Hadoop](https://img.shields.io/badge/Hadoop-HDFS-yellow)
![Cassandra](https://img.shields.io/badge/Cassandra-NoSQL-blue)
![Python](https://img.shields.io/badge/Python-3.8-green)

## 📑 Table of Contents

- Project Overview
- Dataset Description
- Dataset Statistic
- Technology Stack
- Project Workflow
- Analytical Tasks
    - Task 1
    - Task 2
    - Task 3
    - Task 4
    - Task 5
- Visulaization
- Challenges Encountered
- Result Summary
- Conclusion

Data Management Assignment 2
MovieLens Analytics using Apache Zeppelin and Cassandra
Student Information
----------------------------------------------------------------------------------------------------------------------------
Name: Shukeri Jusoh (P156824)

Course: Data Management (STQD6324)

Program: Master of Data Science & Analytics

Platform: Hortonworks Data Platform (HDP 2.6.5)

------------------------------------------------------------------------------------------------------------------------------------

Project Overview
----------------
This project demonstrates the use of Apache Spark to analyze the MovieLens 100K dataset. The objective is to process movie ratings and user demographic data stored in Hadoop Distributed File System (HDFS) and generate meaningful insights through distributed data processing.

Apache Zeppelin was used as the interactive analytics environment, while PySpark was used to perform data transformation, aggregation, filtering, and analytical operations.

Dataset Description
-------------------
The dataset can be download here : https://grouplens.org/datasets/movielens/100k/

The MovieLens 100K dataset contains movie ratings collected from users and consists of three (3) primary files:

u.data	> User movie ratings

u.user	> User demographic information

u.item	> Movie information and genre categories

Dataset Statistics
------------------

| Item | Count |
|------------|----------|
| Ratings | 100,003 |
| Users | 943 |
| Movies | 1,682 |

## 🛠 Technology Stack
-----------------------
| Technology | Purpose |
|------------|----------|
| Apache Hadoop | Distributed Storage (HDFS) |
| Apache Spark | Data Processing |
| Apache Zeppelin | Interactive Analytics |
| Apache Cassandra | NoSQL Storage |



  <img width="337" height="180" alt="hadoop logo" src="https://github.com/user-attachments/assets/a725f300-7f45-4ed0-bd39-fa288aae084b" /> 
  <img width="344" height="180" alt="image" src="https://github.com/user-attachments/assets/0b2d2290-af73-411c-8947-24a997e1854d" />
  <img width="243" height="180" alt="zeppelin" src="https://github.com/user-attachments/assets/89f6911e-60bb-4407-89e7-e3c5be9a3ac3" />
  <img width="135" height="90" alt="cassandra" src="https://github.com/user-attachments/assets/655d0ac5-3cf5-4f52-966a-180b347fbcab" />

Project Workflow
----------------
Verify MovieLens dataset availability in HDFS.
Load MovieLens data into Spark DataFrames.
Perform data quality verification.
Execute analytical tasks.
Visualize analytical results using Zeppelin.
Interpret findings and summarize insights.

<img width="714" height="474" alt="Screenshot 2026-06-12 012551" src="https://github.com/user-attachments/assets/9d912e83-d6a5-4d33-a0c5-f3ee74eb3b2f" />


Analytical Tasks
----------------

Task (i): Average Rating for Each Movie
---------------------------------------
<img width="346" height="257" alt="image" src="https://github.com/user-attachments/assets/15017361-2733-45d0-9c08-ef2a0ecc823d" />

The average rating for each movie was calculated using all available user ratings.

<img width="529" height="262" alt="Task1_average_rating" src="https://github.com/user-attachments/assets/746f4d7d-3d59-4856-9e77-2ce4c97f7e8b" />

<img width="1884" height="459" alt="Task1_average_rating_table" src="https://github.com/user-attachments/assets/b98b491a-85db-4ce0-9c7e-bad29b5b91f5" />


### Interpretation

The average rating for each movie was calculated using all ratings submitted by users. This metric provides an overall measure of audience satisfaction and allows movies to be compared based on their perceived quality. Movies with higher average ratings generally indicate stronger user preference, while lower ratings suggest less favourable reception.

Task (ii): Top 10 Highest Rated Movies
--------------------------------------
Movies were ranked based on their average ratings to identify the highest-rated titles.

<img width="512" height="209" alt="Task2_top10_highest rating" src="https://github.com/user-attachments/assets/bed98075-d4fe-4d32-9b35-05c24cb35df5" />

<img width="1887" height="767" alt="Task2_top10_highest rating_visualization" src="https://github.com/user-attachments/assets/b6d4d77e-1ed3-40e9-a6e7-d9577c5151da" />



### Interpretation

The results show the ten movies with the highest average ratings. Movies with consistently high ratings indicate strong audience appreciation and satisfaction. Including the number of ratings provides additional context, as movies with a large number of ratings and high averages can be considered more reliable indicators of popularity and quality than movies rated by only a few users.

Task (iii): Active Users and Favourite Genres
---------------------------------------------
Users who rated at least 50 movies were classified as active users. Their favourite genre was determined based on the genre they rated most frequently.

<img width="275" height="266" alt="Task3_activeuser_favgenre" src="https://github.com/user-attachments/assets/d39a6f00-4996-41c3-bcd4-8b8b9375178b" />

<img width="1874" height="511" alt="Task3_activeuser_favgenre_visualization_2" src="https://github.com/user-attachments/assets/487e9de2-df2e-4d04-8d0c-682226450ba9" />

<img width="1876" height="392" alt="Task3_activeuser_favgenre_visualization" src="https://github.com/user-attachments/assets/9ec23093-a8f1-4552-ba84-2cb89caafc56" />

### Interpretation

The analysis identified users who rated at least 50 movies and classified them as active users. The favourite genre for each active user was determined by counting how frequently each movie genre appeared among the movies they rated. The results show that Drama is the most common favourite genre among highly active users, indicating a strong preference for story-driven and character-focused films. Other genres such as Comedy and Action also appear among some users, highlighting the diversity of viewing preferences within the MovieLens dataset. This analysis provides useful insights into user behaviour and genre popularity among engaged movie viewers.

Task (iv): Users Below 20 Years Old
-----------------------------------
Users younger than 20 years old were extracted from the dataset.

<img width="302" height="287" alt="Task4_user_below20" src="https://github.com/user-attachments/assets/ad639165-6817-435f-b544-2a6c8d777125" />

<img width="1877" height="417" alt="Task4_user_below20_visualization" src="https://github.com/user-attachments/assets/e2bf7e90-b357-4223-9dfe-2d92be74e921" />

### Interpretation

The results display users whose age is below 20 years old. This group represents younger users within the MovieLens dataset and may exhibit different viewing preferences compared to older age groups. Understanding the demographic composition of users can support further audience segmentation and recommendation analysis.


Task (v): Scientists Aged Between 30 and 40 Years Old
-----------------------------------------------------
Users with occupation listed as scientist and age between 30 and 40 years old were identified.

<img width="293" height="287" alt="Task5_scientist_age_30to40" src="https://github.com/user-attachments/assets/312d2458-e4ef-4dcc-9c21-2dc8dd1963be" />

<img width="1882" height="406" alt="Task5_scientist_age_30to40_visualization" src="https://github.com/user-attachments/assets/20127faf-9ac1-45f5-9ac4-ef227e5ce91f" />

Interpretation
The analysis identified users whose occupation is recorded as scientist and whose age falls between 30 and 40 years old. This subset of users represents a specific demographic group that may be useful for targeted behavioural analysis or recommendation studies. The results demonstrate how Spark can be used to efficiently filter records based on multiple conditions.

Visualizations
--------------
The analytical results were visualized using Apache Zeppelin's built-in visualization tools.

Challenges Encountered
----------------------
During the project implementation several technical challenges were encountered:

- Configuring Spark and Zeppelin interpreters.
- Managing Hadoop services within a virtualized environment.
- Working with Spark DataFrame transformations and joins.
- Investigating Cassandra integration within HDP Sandbox.
- Handling compatibility issues with older Cassandra installation repositories.

These challenges provided valuable experience in troubleshooting distributed data processing environments.

Results Summary
--------------
Task	                          > Result

Average Rating Per Movie	      > Completed

Top 10 Highest Rated Movies	    > Completed

Active Users & Favourite Genre  > Completed

Users Below 20 Years Old	      > 77 Users

Scientists Aged 30-40	          > 16 Users

Conclusion
----------
This project successfully applied Apache Spark to analyze the MovieLens 100K dataset. The analytical tasks provided insights into movie ratings, user demographics, and viewing preferences. The results demonstrated the effectiveness of distributed data processing using Apache Spark and highlighted how large datasets can be transformed into meaningful information for decision-making and recommendation systems.

Overall, the project strengthened practical skills in Hadoop, Spark, HDFS, Zeppelin, and big data analytics workflows.












