from flask import Flask
from flask_restful import Api, Resource, reqparse
import mysql.connector
import datetime
import json
from clsOperation import clsOperation

app = Flask(__name__)

#### Connexion a la base de données SQL
try:
    sqlConnector = mysql.connector.connect(host='localhost',user='pierre',database='gestpea',password='Mroucky_93')
except:
    print("ERROR: Cannot open mySQL database")
sqlCursor = sqlConnector.cursor(buffered = True)

#### Suppression de la table (pour etre sur de recommencer à 0)
# sqlCursor.execute('DROP TABLE IF EXISTS lisOperations')

#### Création de la table de la liste des opérations si elle n'existe pas
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
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;''')

api = Api(app)

ai_quotes = [
    {
        "id": 0,
        "author": "Kevin Kelly",
        "quote": "The business plans of the next 10,000 startups are easy to forecast: " +
                 "Take X and add AI." 
    }
]

#### 
operation_put_args = reqparse.RequestParser()
# operation_put_args.add_argument("Numero", type=str, help="Numero de l'opération",location="json")
operation_put_args.add_argument("Numero", type=int, help="Numero de l'opération",location="json")
# operation_put_args.add_argument("Date", type=date,help="Date de l'opération",required=True)
# operation_put_args.add_argument("Type", type=str,help="Type de l'opération",required=True)
# operation_put_args.add_argument("Nombre", type=int,help="Nombre de titres concernés par l'opération")
# operation_put_args.add_argument("Nom", type=int,help="Nom du titre de l'opération",required=True)
# operation_put_args.add_argument("Montant", type=double,help="Montant de l'opération",required=True)
# operation_put_args.add_argument("Commentaires", type=str,help="Commentaires concernant l'opération")
# operation_put_args.add_argument("Ignore", type=bool,help="Prise en compte ou pas de l'opération")

##### Classe de gestion des opérations
class apiOperation(Resource):
#### Récuperation d'une opération
    def get(self, strAPI):

        intNumeroOperation = None
        try:
            intNumeroOperation = int(strAPI)
        except:
            if strAPI.lower() == "all":
                sqlRequete = 'SELECT * FROM lisOperations;'
            elif strAPI.lower() == "last":
                intNumeroOperation = -1
        #### Ajouter possibilité de retourner toutes les opérations d'un titre

        if intNumeroOperation == -1:
#### Récupération du numero de la dernière opération de la table
            sqlRequete = 'SELECT * FROM lisOperations ORDER BY intNumero DESC LIMIT 1;'
        elif intNumeroOperation != None:
#### Récupération du numero de la dernière opération de la table
            sqlRequete = 'SELECT * FROM lisOperations WHERE intNumero = '+ str(intNumeroOperation) +';'

#### Execution de la requete
        sqlCursor.execute(sqlRequete)
        sqlResponse = sqlCursor.fetchall()
#### Get all the operations from the sql query
        lisOperations = [] #Liste des operations
        for result in sqlResponse:
            lisOperations.append(clsOperation(result))
#### Transform to JSON to send it back
        returnJSON = [] # Response that we want to send
        for operation in lisOperations:
            returnJSON.append(operation.getJSON())
        return returnJSON,200

# #### Récuperation d'une opération
#     def get(self, intNumeroOperation=0):
#         if intNumeroOperation == -1:
# #### Récupération du numero de la dernière opération de la table
#             sqlRequete = 'SELECT * FROM lisOperations ORDER BY intNumero DESC LIMIT 1;'
#         else:
# #### Récupération du numero de la dernière opération de la table
#             sqlRequete = 'SELECT * FROM lisOperations WHERE intNumero = '+ str(intNumeroOperation) +';'
# #### Execution de la requete
#         sqlCursor.execute(sqlRequete)
#         sqlResponse = sqlCursor.fetchall()
# #### Get all the operations from the sql query
#         lisOperations = [] #Liste des operations
#         for result in sqlResponse:
#             lisOperations.append(clsOperation(result))
# #### Transform to JSON to send it back
#         returnJSON = [] # Response that we want to send
#         for operation in lisOperations:
#             returnJSON.append(operation.getJSON())
#         return returnJSON,200


#### Rajout d'une opération
    def put(self, intNumeroOperation):
        print("Numero trouvé ici: "+str(intNumeroOperation))
        args = operation_put_args.parse_args()
        print("Print ici:"+str(args))
        return {"Reponse":"Numero Operation= "+str(intNumeroOperation)+" XXX NumeroInput= "+str(args["Numero"])}, 201

#### Modification d'une opération
    def post(self, intNumeroOperation):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()
        for quote in ai_quotes:
            if(intNumeroOperation == quote["intNumeroOperation"]):
                return f"Quote with id {intNumeroOperation} already exists", 400
        quote = {
            "id": int(intNumeroOperation),
            "author": params["author"],
            "quote": params["quote"]
        }
        ai_quotes.append(quote)
        return quote, 201

#### Suppression d'une opération
    def delete(self, intNumeroOperation):
        global ai_quotes
        ai_quotes = [qoute for qoute in ai_quotes if qoute["intNumeroOperation"] != intNumeroOperation]
        return f"Quote with id {intNumeroOperation} is deleted.", 200


# api.add_resource(apiOperation, "/", "/operation", "/operation/", "/operation/<int:intNumeroOperation>")
api.add_resource(apiOperation, "/", "/operation", "/operation/", "/operation/<string:strAPI>")
if __name__ == '__main__':
    app.run(debug=True)
    # app.run()