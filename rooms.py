#!C:/Users/Psquare World/PycharmProjects/SQL-1/venv/Scripts/python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
room_no = form.getvalue('room_no')
r_type = form.getvalue('r_type')
r_location = form.getvalue('r_location')
price= form.getvalue('price')
max_occu= form.getvalue('max_occu')
dependents=form.getvalue('dependents')


import pymysql
db = pymysql.connect("localhost","root","MH14bv7740","project2" )
cursor = db.cursor()
#data =cursor.execute("select max(cid)+1 from customer")
#print("your id_prof is :",data)

cursor.execute("INSERT INTO rooms(room_no,r_type,r_location,price,max_occu,dependents) VALUES (%s,%s,%s,%s,%s,%s)",(room_no,r_type,r_location,price,max_occu,dependents))
db.commit()

# Execute SQL select statement
#sql_query="SELECT DISTINCT c.cid,c.first_name,c.last_name,c.age,c.id_prof,c.room_no,c.event_id from customer c WHERE TRUE"
#cursor.execute(sql_query)

#sql_query_rooms="SELECT DISTINCT r.room_no,r.r_type,r.r_location,r.price,r.max_occu from rooms r WHERE r.room_no not in(select c.room_no from customer c)"
#cursor.execute(sql_query_rooms)

# Get the number of rows in the resultset
#data=cursor.fetchall()






