
import pandas as pd #Librairie de gestion de tableau
import mysql.connector
import sys


try:
        connexion = mysql.connector.connect(
        # host="127.0.0.1",# host="54.37.9.75",
        user="pierre",password="Mroucky_93",auth_plugin='mysql_native_password',
        database="gestpea"
    )
except mysql.connector.Error as e:
    print(f"Error connecting to mySQL Server: {e}")
    sys.exit(1)

# # Get Cursor
# cur = connexion.cursor()

strURL = "https://query1.finance.yahoo.com/v7/finance/download/OVH.PA?period1=1646989200&period2=999999999999&interval=1d&events=history"
strURL = "https://query1.finance.yahoo.com/v7/finance/download/OVH.PA?period1=1646989200&period2=999999999999"
data = pd.read_csv(strURL)
# print(data)
