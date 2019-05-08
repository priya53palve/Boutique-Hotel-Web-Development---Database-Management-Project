#!C:/Users/Psquare World/PycharmProjects/SQL-1/venv/Scripts/python.exe -u
print("Content-Type: text/html")
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
name = form.getvalue('fname')

import pymysql

# Open connection to the database
db = pymysql.connect("localhost","root","MH14bv7740","project2")

# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method. This should return all the columns of heroes that use swords.
cursor.execute(name)

# Fetch all the rows using fetchall() method.
name = cursor.fetchall()

attribute_names = [i[0] for i in cursor.description]


print("<style>table { font-family: arial, sans-serif; border-collapse: collapse; width: 100%; } td, th { border: 1px solid #dddddd; text-align: left; padding: 8px; } tr:nth-child(even) { background-color: #dddddd; } </style>")
print("<table><tr>")

for columns in attribute_names:
    print("<th>",columns,"</th>")
print ("</tr>")

for rows in name:
    print ("<tr>");
    for subrows in rows:
        print("<td>",subrows,"</td>")
    print ("</tr>")
print("</table>")


# disconnect from server
db.close()