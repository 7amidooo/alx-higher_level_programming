#!/usr/bin/python3

import MySQLdb
import sys

arg = sys.argv
print(arg[2])
dp = MySQLdb.connect(host="localhost", user=f"${arg[1]}",
                     passwd=f"${arg[2]}", database=f"${arg[3]}")
cur = dp.cursor()
for dps in cur:
    print(dps)
