# Creating database connection: https://www.w3schools.com/python/python_mysql_getstarted.asp
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  passwd="python",
  database="PythonTraining"
)
print(mydb)

# Creating database & table
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase2")

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Insert operation
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()
print(mycursor.rowcount, "record inserted.")

# Read\Update\Delete\Commit\Rollback operations
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
print(myresult)

mycursor.close()
mydb.close()