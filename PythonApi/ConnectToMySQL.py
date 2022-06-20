import mysql.connector

##### Connexion a la base de données SQL
try:
    sqlConnector = mysql.connector.connect(host='localhost',user='pierre',database='gestpea',password='Mroucky_93')
except:
    print("ERROR: Cannot open mySQL database")
# print(sqlConnector)

sqlCursor = sqlConnector.cursor(buffered = True)