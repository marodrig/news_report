# Log Analysis tool

This is a python script that creates three reports for a Postgre database.

## Reports created

### Three most popular articles

Prints a table containing a column witht the Article title, and a second column sith the number of views of the corresponding article. Sorted in descending order.

#### Example Output for Three Most Popular articles: NOT THE ACTUAL REPORT

|                      Title                    |  Views  |
|:----------------------------------------------|:-------:|
|Princess Shellfish Marries Prince Handsome     |  1201   |
|Baltimore Ravens Defeat Rhode Island Shoggoths |   915   |
|Political Scandal Ends In Political Scandal    |   600   |

### Most popular article authors of all time

Article author names and views for all articles written by that author. Sorted in descending order and limited to 5 results for performance.

#### Example Output for Most Popular Article Authors: NOT THE ACTUAL REPORT

|          Name          |  Views  |
|:-----------------------|:-------:|
|Ursula La Multa         | 2304    |
|Rudolf von Treppenwitz  | 1985    |
|Markoff Chaney          | 1723    |
|Anonymous Contributor   | 1023    |

### Days with requests error status largest than 1% of request

Print out of date(Format: YYYY-MM-DD) and percent of total request that return 404 NOT FOUND for that day, if this percentage was greater than 1%.

#### Example output: NOT THE ACTUAL REPORT

|          Date          |  Error %  |
|:-----------------------|:---------:|
|2016-07-29              | 2.5%      |

### Views used when creating report

Two views were created when in order to reduce code repetition. One is the popular\_articles\_view and the second one is the percent\_error\_view. Both can be found in the file create\_views.sql, but for convenience purposes we describe them bellow:

#### View: Popular articles

```sql
CREATE VIEW popular_articles_view AS 
    SELECT title, author, count(*) AS num_views 
    FROM articles, log 
    WHERE log.path LIKE concat('/article/',articles.slug)
    GROUP BY title, author; 
```

#### View: Percent error

```sql
CREATE VIEW percent_error_view AS
    SELECT time::date as log_time, ROUND(
        (100*SUM(CASE log.status WHEN '404 NOT FOUND' THEN 1 ELSE 0 END))::numeric/
        count(log.status), 2) as error_percent
    FROM log
    GROUP BY log_time;
```

## Requirements

### Postgre

You need to postgre running in a virtual machine or your machine in order to create the database and interact with it using Python.

### Python

Python is the language used by the log data analysis script.

### Data for the database

You can download the necessary file 
[Here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Usage

Once you have postgre installed, and you have downloaded and unzipped the newsdata.sql file you will need to type the following commands:

    1. Create the postgre database using the newsdata.sql file.

``` cmd
psql -d news -f newsdata.sql
```

    2. Create views using the create_views.sql from this repo.

```cmd
psql -d news -f create_views.sql
```

## License
