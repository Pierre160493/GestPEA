import pandas
import mysql.connector

#######################################################################################################################
class clsTitre: #Classe d'un titre
    def __init__(self,intNumero,operation,strCodeYahoo):
        self.intNumero = intNumero #Numero du titre
        self.strNom = operation["strNom"] #Nom du titre
        self.strCodeYahoo = strCodeYahoo #Code pour le lien Yahoo
        self.lisOperations = []
        self.lisOperations.append(clsOperation(operation)) #Première opération de ce titre
        self.lisCours = [] #Liste des cours
#######################################################################################################################
class clsOperation: #Classe d'une opération
    def __init__(self,operation):
        self.intNumero = operation["intNumero"] #Numero de l'operation
        self.datDate = operation["datDate"] #Date de l'opération
        self.strType = operation["strType"] #Type de l'operation (Achat,RachatDividende,Dividende,Vente)
        self.intNombre = operation["intNombre"] #Nombre de titre concerné
        self.douMontant = operation["douMontant"] #Montant de l'opération
        self.strCommentaire = operation["strCommentaire"] #Commentaire éventuel concernant cette opération
#######################################################################################################################

try:
    # lisOperationsCSV = pandas.read_csv('/home/pierre/GestPEA/lisOperations.csv',sep=';',dtype=str,na_filter=False)
    lisOperationsCSV = pandas.read_csv('/home/pierre/GestPEA/lisOperations.csv',sep=';',na_filter=True,
        usecols = ['intNumero','datDate','strType','intNombre','strNom','douMontant','strCommentaires','booIgnore'],
        dtype={'intNumero':str,'datDate':str,'strType':str,'intNombre':str,'strNom':str,'douMontant':str,'strCommentaires':str,'booIgnore':str})
except:
    print("ERROR: Cannot open the csv file containing the list of the operations")
lisOperationsCSV.fillna('NULL', inplace=True)
print(lisOperationsCSV)

##### Connexion a la base de données SQL
try:
    sqlConnector = mysql.connector.connect(host='localhost',user='pierre',database='gestpea_test',password='Mroucky_93')
except:
    print("ERROR: Cannot open mySQL database")

sqlCursor = sqlConnector.cursor(buffered = True)

##### Suppression de la table (pour etre sur de recommencer à 0)
sqlCursor.execute('DROP TABLE IF EXISTS lisOperations')

##### Création de la table de la liste des opérations si elle n'existe pas
sqlCursor.execute('''CREATE TABLE IF NOT EXISTS lisOperations (
    intNumero int unsigned NOT NULL,
    datDate datetime NOT NULL,
    strType varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
    intNombre int unsigned DEFAULT NULL,
    strNom varchar(50) DEFAULT NULL,
    douMontant double NOT NULL,
    strCommentaires varchar(255) DEFAULT NULL,
    booIgnore tinyint(1) NOT NULL DEFAULT 0,
PRIMARY KEY (intNumero))
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
''')

##### Récupération du numero de la dernière opération de la table
# sqlCursor.execute('SELECT intNumero FROM lisOperations ORDER BY intNumero DESC LIMIT 1;')
# intLastOperationInSQL = sqlCursor.fetchone()[0]
# if intLastOperationInSQL is None : intLastOperationInSQL = 0
intLastOperationInSQL = 0

##### Récupération du numero de la derniere opération du fichier .csv
intLastOperationInCSV = int(lisOperationsCSV['intNumero'].iloc[-1])
# print(intLastOperationInCSV)

# sqlCursor.execute('''INSERT INTO lisOperations VALUES (1,'2018-08-28','Achat',4,'AIRBUS',437.59,NULL)''')
# sqlCursor.execute('''INSERT INTO lisOperations VALUES (1,STR_TO_DATE('28/08/2018 00:00','%d/%m/%Y %H:%i'),'Achat','NULL','AIRBUS',437.59,NULL,1)''')
# sqlConnector.commit()
##### Facon plus propre de faire
# sql = "INSERT INTO lisOperations VALUES (%s,STR_TO_DATE(%s,'%d/%m/%Y %H:%i'),%s,%s,%s,%s,%s,%s)"
# val = []
# # val.append(("1","28/08/2018 00:00","Achat","4","AIRBUS","437.59",""))
# while intLastOperationInSQL < intLastOperationInCSV:
#     val.append(tuple(lisOperationsCSV.iloc[intLastOperationInSQL]))
#     intLastOperationInSQL += 1
# sqlCursor.executemany(sql, val)
# sqlConnector.commit()

##### Facon un peu plus sale
while intLastOperationInSQL < intLastOperationInCSV:
    row = lisOperationsCSV.iloc[intLastOperationInSQL]
    sql = "INSERT INTO lisOperations VALUES ("+row['intNumero']+",STR_TO_DATE('"+row['datDate']+"','%d/%m/%Y %H:%i'),'"+row['strType']+"',"+row['intNombre']+",'"+row['strNom']+"',"+row['douMontant']+","+row['strCommentaires']+","+row['booIgnore']+")"
    sqlCursor.execute(sql)
    intLastOperationInSQL += 1
sqlConnector.commit()

##### Gestion de la liste des opérations pour en extraire la liste des titres
# lisTitres = {"lisTitres": []} #Initialisation de la liste
# for operation in inputData["lisOperations"]: #Boucle sur la liste des opérations pour en extraire la liste des titres
#     for titre in lisTitres["lisTitres"]: #Boucle sur la liste des titres pour chercher si une opération a deja concernée ce titre
#         if titre.strNom == operation["strNom"]: #Si ce titre existe deja
#             titre.lisOperations.append(operation) #On ajoute l'opération à la liste
#             break #On passe à l'opération suivante
#     else: #Si on arrive la c'est qu'il s'agit de la première opération sur ce titre
#         for codeYahoo in inputData["lisCodeYahoo"]: #Boucle sur la liste des codes Yahoo pour chercher le code correspondant à ce titre
#             if codeYahoo.get("strNom") == operation.get("strNom"): #Si les noms correspondent
#                 lisTitres["lisTitres"].append(clsTitre(len(lisTitres["lisTitres"])+1,operation,codeYahoo.get("strCode"))) #On ajoute ce nouveau titre à la liste des titres
#                 break #On quitte la boucle
#         else: #Si on arrive la c'est qu'aucun code Yahoo n'a été trouvé, erreur !
#             lisTitres["lisTitres"].append(clsTitre(len(lisTitres["lisTitres"])+1,operation,None)) #On ajoute ce nouveau titre à la liste des titres

# with open(r'C:\Users\pierr\Google Drive\Projets\Bourse_PEA\Python\lisTitres.json',"w") as file: #Ecriture de la liste dans un fichier
#     json.dump(lisTitres,file,default=lambda o: o.__dict__, indent=2) #En format JSON