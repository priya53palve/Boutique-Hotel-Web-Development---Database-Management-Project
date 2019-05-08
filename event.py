#!C:/Users/Psquare World/PycharmProjects/SQL-1/venv/Scripts/python.exe -u

print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
event_id= form.getvalue('event_id')
e_type= form.getvalue('e_type')
e_date= form.getvalue('e_date')

import pymysql
db = pymysql.connect("localhost","root","MH14bv7740","project2" )
cursor = db.cursor()
#data =cursor.execute("select max(event_id)+1 from events")
#print("your e_type is :",data)
cursor.execute("INSERT INTO events(event_id,e_type,e_date) VALUES (%s,%s,%s)",(event_id,e_type,e_date))
db.commit()

# Execute SQL select statement
sql_query1="SELECT DISTINCT e.event_id ,e.e_type,e.e_date from events e WHERE TRUE"
cursor.execute(sql_query1)

# Get the number of rows in the resultset
data = cursor.fetchall()

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