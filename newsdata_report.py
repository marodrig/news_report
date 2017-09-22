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
    """:returns : Connection object to the database specified in DBNAME"""
    return psycopg2.connect(database=DBNAME)


def get_days_with_errors():
    """":returns : list of tuples of dates and error percentage."""
    return get_qry_result(DAYS_WITH_ERROR_QRY)


def get_popular_authors():
    """:returns : list of tuples of author names and total views."""
    return get_qry_result(FAVORITE_AUTHORS_QRY)


def get_most_popular_articles():
    """:returns list: list of tuples with three most favorite articles."""
    return get_qry_result(FAVORITE_ARTICLES_QRY)


def get_qry_result(qry):
    """
    :param qry: string of the sql query to be executed

    :returns tuple_list: list of tuples with the result of the query specified by the string qry 
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute(qry)
    result_list = cur.fetchall()
    conn.close()
    return result_list


def print_days_with_errors():
    """Prints table with date (YYYY-MM-DD) and error percentage, if error percentage is greater than 1%."""
    days_with_errors_list = get_days_with_errors()
    print(" -" * 12)
    print("|{:^12}|{:^8} |".format("Date", "Error %"))
    print(" -" * 12)
    for item in days_with_errors_list:
        print("| {} |{:^8}%|".format(item[0], item[1]))
    print(" -" * 12)


def print_report(result_list, header_tuple):
    """
    Prints a report using a list and column headers from a tuple.

    :param result_list: list of tuples from a query result

    :param header_tuple: Tuples with the column headers
    """
    print(" -" * 22)
    print("|{:^32}|{:^8} |".format(header_tuple[0], header_tuple[1]))
    print(" -" * 22)
    for item in result_list:
        print("|{:<32}|{:^8} |".format(item[0], item[1]))
    print(" -" * 22)


def print_popular_articles():
    """Tabulated print out of three most popular articles."""
    popular_articles_list = get_most_popular_articles()
    print_report(popular_articles_list, ("Article title", "Views"))


def print_popular_authors():
    """Tabulated print out popular authors."""
    popular_authors_list = get_popular_authors()
    print_report(popular_authors_list, ("Authors Name", "Views"))


if __name__ == '__main__':
    print_popular_articles()
    print_popular_authors()
    print_days_with_errors()
