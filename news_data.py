#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

query1_question = ("What are the most popular three articles of all time?")
query1 = ("select articles.title, count(log.path) as views "
          "from articles,log "
          "where log.path like'%'||articles.slug "
          "and log.status like '%200%' "
          "group by articles.title "
          "order by views desc limit 3;")

query2_question = ("Who are the most popular article authors of all time?")
query2 = ("select name, views from authors,articlesauthors_v "
          "where authors.id = articlesauthors_v.author;")

query3_question = ("On which days did more than 1% of requests lead "
                   "to errors?")

query3 = ("select * from rate_val where val > 1;")


def connect_database():

        """Connect to the Postgres database and returns a database """
        """ connection"""

        try:
                db = psycopg2.connect(database=DBNAME)
                c = db.cursor()
                return db, c

        except:

                print("Not able to connect to the database")


def get_results(query):

        """Return query results for the query"""

        db, c = connect_database()
        c.execute(query)
        return c.fetchall()
        db.close()


def print_results(results):

        """Print the results for query 1 and query 2"""

        print(results[1])

        for row in results[0]:
            print("- " + row[0] + " - " + str(row[1]) + " views")


def print_error_results(results):

        """Print the results for query3"""

        print(results[1])

        for row in results[0]:
            print("- " + str(row[0]) + " - " + str(row[1]) + "% errors")


if __name__ == '__main__':

        popular_articles = get_results(query1), query1_question
        popular_authors = get_results(query2), query2_question
        error_days = get_results(query3), query3_question

        print_results(popular_articles)
        print_results(popular_authors)
        print_error_results(error_days)
