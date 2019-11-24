#Based off of: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
import mysql.connector

cnx = mysql.connector.connect(user='strong', 
							password='password3',
							host='localhost',
							database='assignment4')

cursor = cnx.cursor()
example = ('SELECT * FROM instructor');							

cursor.execute(example)

for (ID, name, dept_name, salary) in cursor:
	print('{} {} {} {}'.format(ID, name, dept_name, salary))

cursor.close()
cnx.close()