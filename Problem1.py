#Author: Noah Wilmoree
#File: Problem1.py
#Date: 11.24.2019
#Purpose: Demonstrates selection, grouping, and average of a table, instructor, by a strong, medium, and weak user through code imbeded in python.

import mysql.connector

strong_connect = mysql.connector.connect(user='strong', 
							password='password3',
							host='localhost',
							database='assignment4')

med_connect = mysql.connector.connect(user='medium', 
							password='password2',
							host='localhost',
							database='assignment4')

weak_connect = mysql.connector.connect(user='weak', 
							password='password1',
							host='localhost',
							database='assignment4')

strong_cursor = strong_connect.cursor()
med_cursor = med_connect.cursor()
weak_cursor = weak_connect.cursor()

select = ('SELECT dept_name, AVG(salary) FROM instructor GROUP BY dept_name');

print('\nStrong select:')
strong_cursor.execute(select)
for (dept_name, salary) in strong_cursor:
	print('{} {}'.format(dept_name, salary))

strong_cursor.close()
strong_connect.close()

print('\nMedium select:')
med_cursor.execute(select)
for (dept_name, salary) in med_cursor:
	print('{} {}'.format(dept_name, salary))

med_cursor.close()
med_connect.close()

print('\nWeak select:')
weak_cursor.execute(select)
for (dept_name, salary) in weak_cursor:
	print('{} {}'.format(dept_name, salary))

weak_cursor.close()
weak_connect.close()