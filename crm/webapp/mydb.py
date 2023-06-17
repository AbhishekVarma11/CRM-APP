import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',

)

cusorObject=dataBase.cursor()
cusorObject.execute("Create database crm")
print("All done")