Data Management Assignment 2
MovieLens Analytics using Apache Zeppelin and Cassandra
Student Information
----------------------------------------------------------------------------------------------------------------------------
Name: Shukeri

Course: Data Management

Program: Master of Data Science & Analytics

Platform: Hortonworks Data Platform (HDP 2.6.5)

----------------------------------------------------------------------------------------------------------------------------

Project Overview
----------------
This project demonstrates the use of Apache Spark to analyze the MovieLens 100K dataset. The objective is to process movie ratings and user demographic data stored in Hadoop Distributed File System (HDFS) and generate meaningful insights through distributed data processing.

Apache Zeppelin was used as the interactive analytics environment, while PySpark was used to perform data transformation, aggregation, filtering, and analytical operations.

Dataset Description
-------------------

The MovieLens 100K dataset contains movie ratings collected from users and consists of three primary files:

File	Description
-----------------
u.data	> User movie ratings

u.user	> User demographic information

u.item	> Movie information and genre categories

Dataset Statistics
------------------
Item	               Count

Ratings            	100,003

Users	                 943

Movies	             1,682

Technologies Used
-----------------
Apache Spark 2.3
Apache Zeppelin
Hadoop HDFS
PySpark
Hortonworks Data Platform (HDP 2.6.5)
Linux (CentOS 7)

Project Workflow
----------------
Verify MovieLens dataset availability in HDFS.
Load MovieLens data into Spark DataFrames.
Perform data quality verification.
Execute analytical tasks.
Visualize analytical results using Zeppelin.
Interpret findings and summarize insights.

Analytical Tasks
----------------

Task (i): Average Rating for Each Movie
---------------------------------------
The average rating for each movie was calculated using all available user ratings.

Key Finding :
Most movies received average ratings between 3.0 and 4.0, indicating generally positive user feedback.

Task (ii): Top 10 Highest Rated Movies
--------------------------------------
Movies were ranked based on their average ratings to identify the highest-rated titles.

Key Finding :
Several movies achieved exceptionally high average ratings, demonstrating strong audience appreciation and satisfaction.

Task (iii): Active Users and Favourite Genres
---------------------------------------------
Users who rated at least 50 movies were classified as active users. Their favourite genre was determined based on the genre they rated most frequently.

Key Finding :
Drama was identified as the most popular favourite genre among active users, followed by Comedy and Action.

Task (iv): Users Below 20 Years Old
-----------------------------------
Users younger than 20 years old were extracted from the dataset.

Key Finding :
A total of 77 users were identified in this age category.

Task (v): Scientists Aged Between 30 and 40 Years Old
-----------------------------------------------------
Users with occupation listed as scientist and age between 30 and 40 years old were identified.

Key Finding :
A total of 16 users met these criteria.

Visualizations
--------------
The analytical results were visualized using Apache Zeppelin's built-in visualization tools.

Favourite Genre Distribution
----------------------------
The visualization shows the distribution of favourite genres among active users.

Observation
-----------
Drama dominates user preferences with 372 active users selecting it as their favourite genre, followed by Comedy (102 users) and Action (72 users).

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












