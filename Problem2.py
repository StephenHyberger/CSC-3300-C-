#Author: Noah Wilmoree
#File: Problem2.py
#Date: 11.24.2019
#Purpose: Demonstrates selection and update of a table, instructor, by a strong and medium user through code imbeded in python.

import mysql.connector

strong_connect = mysql.connector.connect(user='strong', 
							password='password3',
							host='localhost',
							database='assignment4')

med_connect = mysql.connector.connect(user='medium', 
							password='password2',
							host='localhost',
							database='assignment4')

strong_cursor = strong_connect.cursor()
med_cursor = med_connect.cursor()

select = ('SELECT dept_name, salary FROM instructor');
update = ('UPDATE instructor SET salary = salary * 1.2 WHERE salary < 65000');

print('\nTable before:')
strong_cursor.execute(select)
for (dept_name, salary) in strong_cursor:
    print('{} {}'.format(dept_name, salary))

print('\nTable after strong update:')
strong_cursor.execute(update)
strong_cursor.execute(select)
for (dept_name, salary) in strong_cursor:
	print('{} {}'.format(dept_name, salary))

strong_cursor.close()
strong_connect.close()

print('\nTable after medium update:')
med_cursor.execute(update)
med_cursor.execute(select)
for (dept_name, salary) in med_cursor:
	print('{} {}'.format(dept_name, salary))

med_cursor.close()
med_connect.close()