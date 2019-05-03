#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","localdb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("select concat(e.first_name,e.last_name) as employee_name,
t.title as employee_title,
e.gender,e.hire_date,d.dept_name,
concat(e1.first_name,e1.last_name) as manager_name,
t1.title as manager_title
from  employee e right join titles t on e.emp_no = t.emp_no
right join dept_emp de on e.emp_no = de.emp_no
right join departments d on de.dept_no = d.dept_no
right join dept_manager dm on de.dept_no = dm.dept_no
inner join employee e1 on dm.emp_no = e1.emp_no
inner join titles t1 on dm.emp_no = t1.emp_no")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print "Employee Details : %s " % data

# disconnect from server
db.close()