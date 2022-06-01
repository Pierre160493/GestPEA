
import pandas as pd #Librairie de gestion de tableau
# import mariadb
# import sys

# try:
#     conn = mariadb.connect(
#         user="pierre",
#         password="Mroucky_93",
#         host="54.37.9.75",
#         port=3306,
#         database="gestpea"
#     )
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)

# # Get Cursor
# cur = conn.cursor()

strURL = "https://query1.finance.yahoo.com/v7/finance/download/OVH.PA?period1=1646989200&period2=999999999999&interval=1d&events=history"
strURL = "https://query1.finance.yahoo.com/v7/finance/download/OVH.PA?period1=1646989200&period2=999999999999"
data = pd.read_csv(strURL)
print(data)
