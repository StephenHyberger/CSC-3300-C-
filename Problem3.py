#Author: Kristen Forte
#Edited: Stephen Hyberger
#File: Problem3.py
#Date: 11.24.2019
#Purpose: Demonstrates deleting from a table by a strong user through code imbeded in python.
#Based off of: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
#and			http://www.mysqltutorial.org/mysql-delete-statement.aspx
import mysql.connector

strong_connect = mysql.connector.connect(user='strong', 
							password='password3',
							host='localhost',
							database='assignment4')

strong_cursor = strong_connect.cursor()

strong_delete = ('DELETE FROM instructor WHERE dept_name = \'Physics\'');

strong_show = ('SELECT * FROM instructor');

strong_cursor.execute(strong_show)

print()
for (ID, name, dept_name, salary) in strong_cursor:
	print('{} {} {} {}'.format(ID, name, dept_name, salary))


strong_cursor.execute(strong_delete)

strong_cursor.execute(strong_show)

print()
for (ID, name, dept_name, salary) in strong_cursor:
	print('{} {} {} {}'.format(ID, name, dept_name, salary))

strong_cursor.close()
strong_connect.close()