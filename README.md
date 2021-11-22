# Project Data Warehouse
## Project Overview

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In this project, we created an ETL pipeline to build a data warehouses hosted on Redshift. 

## Song Dataset 
We worked with two datasets residing in S3:

#### Song Dataset: 
The first dataset is a subset of real data from [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/). Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID.

Sample Data:
```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

## Log Dataset
The second dataset consists of log files in JSON format generated by this [event simulator](https://github.com/Interana/eventsim) based on the songs in the dataset above. These simulate app activity logs from an imaginary music streaming app based on configuration settings.

The log files in the dataset are partitioned by year and month. 

Sample Data: 
```
{"artist":null,"auth":"Logged In","firstName":"Walter","gender":"M","itemInSession":0,"lastName":"Frye","length":null,"level":"free","location":"San Francisco-Oakland-Hayward, CA","method":"GET","page":"Home","registration":1540919166796.0,"sessionId":38,"song":null,"status":200,"ts":1541105830796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}
```

## Schema for Song Play Analysis

#### Fact Table
##### songplays - records in event data associated with song plays (i.e. records with page 'NextSong'):
    songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

#### Dimension Tables 

##### users - users in the app:
    user_id, first_name, last_name, gender, level

##### songs - songs in music database:
    song_id, title, artist_id, year, duration

##### artists - artists in music database
    artist_id, name, location, lattitude, longitude

##### time - timestamps of records in songplays broken down into specific units
    start_time, hour, day, week, month, year, weekday


## How to Run
#### Launch a Redshift Cluster.

#### Setup Configurations 
Setup the dwh.cfg file (File not added in this repository). File format for **dwh.cfg**

```
[CLUSTER]
HOST=''
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_PORT=5439

[IAM_ROLE]
ARN=<IAM Role arn>

[S3]
LOG_DATA='s3://udacity-dend/log_data'
LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
SONG_DATA='s3://udacity-dend/song_data'
```

#### Create tables
```
    $ python create_tables.py
```

#### Load Data
```
    $ pyton create_tables.py
```