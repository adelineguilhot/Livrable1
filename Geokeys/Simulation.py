import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="DamienQ",
  passwd="Suikenmaster.26",
  database="Geokeys",
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Cles")

for x in mycursor:
    print(x)



