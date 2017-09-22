# News data report python tool

This is a python script that creates three reports for a Postgre database.

## Reports created
1. **Three most popular articles** Prints a table containing a column witht the
Article title, and a second column sith the number of views of the corresponding 
article. Sorted in descending order.

**Example output: NOT THE ACTUAL REPORT**


|                      Title                    |  Views  |
|:----------------------------------------------|:-------:|
|Princess Shellfish Marries Prince Handsome     |  1201   |
|Baltimore Ravens Defeat Rhode Island Shoggoths |   915   |
|Political Scandal Ends In Political Scandal    |   600   |

2. **Most popular article authors of all time** Article author names and views
for all articles written by that author. Sorted in descending order and limited
to 5 results for performance. 

**Example output: NOT THE ACTUAL REPORT**


|          Name          |  Views  |
|:-----------------------|:-------:|
|Ursula La Multa         | 2304    |
|Rudolf von Treppenwitz  | 1985    |
|Markoff Chaney          | 1723    |
|Anonymous Contributor   | 1023    |

3. **Days with requests error status largest than 1% of request** Print out
of date(Format: YYYY-MM-DD) and percent of total request that return 404 NOT FOUND
for that day, if this percentage was greater than 1%.

**Example output: NOT THE ACTUAL REPORT**


|          Date          |  Error %  |
|:-----------------------|:---------:|
|2016-07-29              | 2.5%      |

# Requirements

# Usage

# License
