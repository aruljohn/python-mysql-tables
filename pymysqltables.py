#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""
This script connects to a remote MySQL database
and displays all table names
Coded by Arul John
Created on 22 January 2019
Last Updated: <>
"""

import pymysql

# Credentials
auth = {'username': '****', 'password': '****', 'port': 3306, \
        'database': '****', 'host': 'localhost'}

# Connect to MySQL
db = pymysql.connect(user=auth['username'], password=auth['password'], \
                    database=auth['database'], host=auth['host'], port=auth['port'])
cursor = db.cursor()
sql = 'show tables'
try:
    cursor.execute(sql)
    # Display all table names
    print('LIST OF TABLES')
    for (table,) in cursor:
        print(table), 
except Exception as e:
    print('ERROR: {}'.format(repr(e)))

# Close database connection
cursor.close()
db.close()
