#!C:/Users/Psquare World/PycharmProjects/SQL-1/venv/Scripts/python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
age = form.getvalue('age')
id_prof = form.getvalue('id_prof')
event_id= form.getvalue('event_id')
room_no= form.getvalue('room_no')

import pymysql
db = pymysql.connect("localhost","root","MH14bv7740","project2" )
cursor = db.cursor()
#data =cursor.execute("select max(cid)+1 from customer")
#print("your id_prof is :",data)

cursor.execute("INSERT INTO customer(first_name,last_name,age,id_prof,room_no,event_id) VALUES (%s,%s,%s,%s,%s,%s)",(first_name,last_name,age,id_prof,room_no,event_id))
db.commit()

# Execute SQL select statement
#sql_query="SELECT DISTINCT c.cid,c.first_name,c.last_name,c.age,c.id_prof,c.room_no,c.event_id from customer c WHERE TRUE"
#cursor.execute(sql_query)

#sql_query_rooms="SELECT DISTINCT r.room_no,r.r_type,r.r_location,r.price,r.max_occu from rooms r WHERE r.room_no not in(select c.room_no from customer c)"
#cursor.execute(sql_query_rooms)

# Get the number of rows in the resultset
#data=cursor.fetchall()






