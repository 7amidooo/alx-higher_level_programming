#!/usr/bin/python3
"""  Second using of mysqldb"""
import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    dp = MySQLdb.connect(host="localhost", user=arg[1],
                         passwd=arg[2], db=arg[3], port=3306)
    cur = dp.cursor()
    cur.execute(""" SELECT * FROM states
     WHERE name LIKE BINARY 'N%'
     ORDER BY states.id""")
    result = cur.fetchall()
    for dps in result:
        print(dps)
    cur.close()
    dp.close()
