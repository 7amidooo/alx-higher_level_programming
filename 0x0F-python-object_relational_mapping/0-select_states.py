#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    dp = MySQLdb.connect(host="localhost", user=arg[1],
                         passwd=arg[2], database=arg[3], port=3306)
    cur = dp.cursor()
    cur.execute("select * from states")
    for dps in cur:
        print(dps)
    cur.close()
    dp.close()
