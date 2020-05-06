"""
William Escobar
BCS 109
Python/MySQL: Interactive Dictionary

Remember to install:
pip3 install mysql-connector-python
"""
import mysql.connector

connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = connection.cursor()

word = input("Search for: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

# We use [0] to extract the tuple.
if results:
    for result in results:
        print(results[0])
else:
    print("No word found.")