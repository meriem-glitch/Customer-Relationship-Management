import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="meriem"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")

print ('All done!')
