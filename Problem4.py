#Author: Kristen Forte
#File: Problem4.py
#Date: 11.24.2019
#Purpose: Demonstrates adding a column to a table by a strong user through code imbeded in python.
#Based off of: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
#and			http://www.mysqltutorial.org/mysql-add-column/
import mysql.connector

strong_connect = mysql.connector.connect(user='strong', 
							password='password3',
							host='localhost',
							database='assignment4')

strong_cursor = strong_connect.cursor()

strong_add = ('ALTER TABLE instructor ADD COLUMN office_no VARCHAR(10) AFTER salary');

strong_show = ('SELECT * FROM instructor');

strong_cursor.execute(strong_add)

strong_cursor.execute(strong_show)

for (ID, name, dept_name, salary, office_no) in cursor:
	print('{} {} {} {} {}'.format(ID, name, dept_name, salary, office_no))

strong_cursor.close()
strong_connect.close()