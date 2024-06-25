#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def states(username, userPassword, database_name, state_name):
    """
    Connects to a MySQL database and executes a query to retrieve all states.

    Args:
        username (str): The username to use for the database connection.
        userPassword (str): The password to use for the database connection.
        database_name (str): The name of the database to connect to.

    Returns:
        None

    Raises:
        MySQLdb._exceptions.OperationalError: If the database connection fails.
    """

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=userPassword,
                         db=database_name)

    cur = db.cursor()

    query = ("SELECT cities.name FROM cities " +
             "JOIN states ON cities.state_id = states.id " +
             "WHERE states.name LIKE %s ORDER BY cities.id")

    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    print(", ".join(a[0] for a in rows))

    cur.close()

    db.close()


if __name__ == "__main__":
    """mas cosas"""

    user = sys.argv[1]
    passw = sys.argv[2]
    bd = sys.argv[3]
    name = sys.argv[4]

    states(user, passw, bd, name)
