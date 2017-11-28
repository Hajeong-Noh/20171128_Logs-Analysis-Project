# Python version: 3.6.3
import psycopg2


def main():
    # Connect to the "news" database
    conn = psycopg2.connect(dbname="news")

    # Open a cursor to perform database operations
    cursor = conn.cursor()

    # Log 1: What are the most popular 3 articles?
    query1 = "select title, view from PopularArticles limit 3"
    cursor.execute(query1)

    print("-" * 70)
    print("Most popular 3 articles:")
    for (title, view) in cursor.fetchall():
        print("    {} - {} views".format(title, view))
    print("-" * 70)

    # Log 2 : Who are the most popular 3 authors?
    query2 = "select * from PopularAuthors"
    cursor.execute(query2)

    print("Most popular Authors:")
    for (name, view) in cursor.fetchall():
        print("    {} - {} views".format(name, view))
    print("-" * 70)

    # Log 3 : Which day did more than 1% of requests lead to errors?
    query3 = "select * from ErrorRate"
    cursor.execute(query3)

    print("Days that had more than 1% of request errors:")
    for (date, errorrate) in cursor.fetchall():
        print("    {} - {}% views".format(date, errorrate*100))
    print("-" * 70)

    # Disconnect from the database
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
