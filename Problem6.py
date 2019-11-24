#Author: Stephen Hyberger
#File: Problem6.py
#Date: 11.24.2019
#Purpose: Demonstrating error handling with SQL code embedded inside python code.
#Based on: https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html

import mysql.connector

try:
	server = mysql.connector.connect(user='weak',
									password='password1',
									host='localhost',
									database='assignment4')

	cursor = server.cursor()
	query = ("DELETE FROM instructor WHERE dept_name = 'Phyics'")

	cursor.execute(query)

	cursor.close()								
	server.close()
except mysql.connector.Error as e:
	print("Insufficient authorization level. Delete operation failed.")
	print("MySQL error:\n{}".format(e))