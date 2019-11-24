#Based off of: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
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

strong_select = ('SELECT dept_name, avg(salary) AS average FROM instructor GROUP BY dept_name');
med_select = ('SELECT dept_name, avg(salary) AS average FROM instructor GROUP BY dept_name');
weak_select = ('SELECT dept_name, avg(salary) AS average FROM instructor GROUP BY dept_name');

strong_cursor.execute(strong_select)
med_cursor.execute(med_select)
weak_cursor.execute(weak_select)

for (dept_name, salary) in strong_cursor:
	print('{} {}'.format(dept_name, salary))
for (dept_name, salary) in med_cursor:
	print('{} {}'.format(dept_name, salary))
for (dept_name, salary) in weak_cursor:
	print('{} {}'.format(dept_name, salary))

strong_cursor.close()
strong_connect.close()
med_cursor.close()
med_connect.close()
weak_cursor.close()
weak_connect.close()