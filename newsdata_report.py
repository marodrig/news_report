#!/usr/bin/env python


import psycopg2

DBNAME = "news"

FAVORITE_ARTICLES_QRY = '''SELECT title, num_views
                           FROM popular_articles_view
                           ORDER BY num_views DESC
                           LIMIT 3;
                        '''

FAVORITE_AUTHORS_QRY = '''SELECT authors.name, sum(popular_articles_view.num_views) AS views
                          FROM popular_articles_view, authors
                          WHERE authors.id = popular_articles_view.author
                          GROUP BY authors.name
                          ORDER BY views DESC
                          LIMIT 5;
                      '''

DAYS_WITH_ERROR_QRY = '''SELECT log_time, error_percent
                         FROM percent_error_view
                         WHERE error_percent > 1.00
                         LIMIT 10;
                      '''


def connect():
    """
    Returns a connection object to the database.
    """
    return psycopg2.connect(database=DBNAME)


def get_days_with_errors():
    '''
    Returns days when request had more than 1% of errors.
    '''
    return get_qry_result(DAYS_WITH_ERROR_QRY)


def get_popular_authors():
    '''
    Return a list of popular authors.
    '''
    return get_qry_result(FAVORITE_AUTHORS_QRY)


def get_most_popular_articles():
    """
    Returns a list of the three most popular articles of all time.
    """
    return get_qry_result(FAVORITE_ARTICLES_QRY)


def get_qry_result(qry):
    """
    Returns a list of results based on the query string passed.
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute(qry)
    result_list = cur.fetchall()
    conn.close()
    return result_list


def print_days_with_errors():
    '''
    '''
    days_with_errors_list = get_days_with_errors()
    print(" -" * 12)
    print("|{:^12}|{:^8} |".format("Date", "Error %"))
    print(" -" * 12)
    for item in days_with_errors_list:
        print("| {} |{:^8}%|".format(item[0], item[1]))
    print(" -" * 12)


def print_report(result_list, header_tupple):
    '''
    print method for a list that contains query results.
    '''
    print(" -" * 22)
    print("|{:^32}|{:^8} |".format(header_tupple[0], header_tupple[1]))
    print(" -" * 22)
    for item in result_list:
        print("|{:<32}|{:^8} |".format(item[0], item[1]))
    print(" -" * 22)


def print_popular_articles():
    '''
    Tabulated print out of three most popular articles.
    '''
    popular_articles_list = get_most_popular_articles()
    print_report(popular_articles_list, ("Article title", "Views"))


def print_popular_authors():
    '''
    Tabulated print out popular authors.
    '''
    popular_authors_list = get_popular_authors()
    print_report(popular_authors_list, ("Authors Name", "Views"))


if __name__ == '__main__':
    print_popular_articles()
    print_popular_authors()
    print_days_with_errors()
