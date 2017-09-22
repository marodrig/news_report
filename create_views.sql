--- creates our favorite articles view used to find the
--- three most favorite articles.
DROP VIEW IF EXISTS popular_articles_view;
CREATE VIEW popular_articles_view AS 
    SELECT title, author, count(*) AS num_views 
    FROM articles, log 
    WHERE log.path LIKE concat('/article/',articles.slug)
    GROUP BY title, author; 
---
--- 
DROP VIEW IF EXISTS percent_error_view;
CREATE VIEW percent_error_view AS
    SELECT time::date as log_time, ROUND(
        (100*SUM(CASE log.status WHEN '404 NOT FOUND' THEN 1 ELSE 0 END))::numeric/
        count(log.status), 2) as error_percent
    FROM log
    GROUP BY log_time;
---
---