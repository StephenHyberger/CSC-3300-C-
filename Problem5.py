#Author: Stephen Hyberger
#File: asg4p5.py
#Date: 11.24.2019
#Purpose: Demonstrates removal of a table, course, by a strong user through code imbeded in python.

import mysql.connector

server = mysql.connector.connect(user='strong',
							password='password3',
							host='localhost',
							database='assignment4')

cursor = server.cursor()
query = ('SHOW TABLES')
cursor.execute(query)

print('\nTables before:')
for(item) in cursor:
	print(item)

query = ('DROP TABLE IF EXISTS course')
cursor.execute(query)

print('\nRemoved course table from database')

query = ('SHOW TABLES')
cursor.execute(query)

print('\nTables after:')
for(item) in cursor:
	print(item)

cursor.close()
server.close()