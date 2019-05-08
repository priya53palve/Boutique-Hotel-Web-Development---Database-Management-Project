#!C:/Users/Psquare World/PycharmProjects/SQL-1/venv/Scripts/python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()

import pymysql
db = pymysql.connect("localhost","root","MH14bv7740","project2" )
cursor = db.cursor()
#data =cursor.execute("select max(cid)+1 from customer")
#print("your id_prof is :",data)
#room_no=000
#cursor.execute("INSERT INTO customer(first_name,last_name,age,id_prof,room_no,event_id) VALUES (%s,%s,%s,%s,%s,%s)",(first_name,last_name,age,id_prof,room_no,event_id))
#db.commit()

# Execute SQL select statement
#sql_query="SELECT DISTINCT c.cid,c.first_name,c.last_name,c.age,c.id_prof,c.room_no,c.event_id from customer c WHERE TRUE"
#cursor.execute(sql_query)

sql_query_rooms=" select distinct c.cid,c.first_name,c.last_name,c.age,c.id_prof,c.room_no,r.r_type,r.r_location,r.price,r.max_occu,r.dependents,b.bid,b.event_id,b.no_guest,b.checkin,b.checkout,e.e_type,e.e_date,p.pay_type,p.discount,p.total from customer c,rooms r, booking b,events e,payment p WHERE c.room_no = r.room_no AND c.cid=b.cid AND c.event_id = e.event_id AND b.bid=p.bid;"
cursor.execute(sql_query_rooms)

# Get the number of rows in the resultset
data=cursor.fetchall()

attribute_names = [i[0] for i in cursor.description]

print("<style>table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } tr:nth-child(even) { background-color: #dddddd; } </style>")
print("<table><tr>")

for columns in attribute_names:
    print("<th>",columns,"</th>")
print ("</tr>")

for rows in data:
    print ("<tr>");
    for subrows in rows:
        print("<td>",subrows,"</td>")
    print ("</tr>")
print("</table>")
