import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rovin123",
  database="iitgn_hostel"
)

mycursor = mydb.cursor()
type_lst = ["chair", "table", "bed", "bunk bed", "almirah", "shoe rack", "drawers"]
room_no_lst = list(range(101,499))

for i in range (1,100):

  sql = "INSERT INTO furniture (furniture_id, type, price, room_no) VALUES (%s, %s, %s , %s )"
  val = (i*1000+i, random.choice(type_lst), (i*989898+4)%99999, random.choice(room_no_lst))
  mycursor.execute(sql, val)


# working_days_lst = ["MONDAY", "TUESDAY", "WEDNESDAY","THRUSDAY", "FRIDAY","SATURDAY","SUNDAY"]
# # block_name_lst = ["A","B","C","D","E","F","G","H","I","J","K"]

# for i in range (1,1000):

#   sql = "INSERT INTO staff_works_for (block_name, staff_id, working_days) VALUES (%s, %s, %s )"
#   val = ((i%9)+1, i*100+i, random.choice(working_days_lst))
#   mycursor.execute(sql, val)


# sql = "INSERT INTO student (roll_no, name, branch, street) VALUES (%s, %s,%s , %s)"
# val = (305, "ROVIN", "AI", "ST_GeomFromText('POINT(1 1)')")
# mycursor.execute(sql, val)
# VALUES (303, "ROVIN", "AI", ST_GeomFromText('POINT(1 1)'));


mydb.commit()