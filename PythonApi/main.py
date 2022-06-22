from urllib import response
from flask import Flask
from flask_restful import Api, Resource, reqparse
import mysql.connector
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

##### Operations API
class apiOperation(Resource):
#######################################################################################################################
#######################################################################################################################
#### GET an operation
    def get(self, strAPI= ""):

        sqlRequest = 'SELECT * FROM lisOperations;' # By default we return all the operations
        intNumeroOperation = None # By default there is no specific number of operation to return
        try: # We try to get an int number to return a specific number of operation
            intNumeroOperation = int(strAPI)
        except: # If it fails we check for the "last" keyword to return the last operation stored in the db
            if strAPI.lower() == "last":
                intNumeroOperation = -1
            #### Add the possibility to get all the operations of a specific stock !!
#### Handling of the sql request for specific cases to return specific number of operation
        if intNumeroOperation == -1: # Then we want the last operation stored in the db
            sqlRequest = 'SELECT * FROM lisOperations ORDER BY intNumero DESC LIMIT 1;'
        elif intNumeroOperation != None: # Then we want a specific number of operation
            sqlRequest = 'SELECT * FROM lisOperations WHERE intNumero = '+ str(intNumeroOperation) +';'

        sqlCursor.execute(sqlRequest) # Execution of the sql request
#### Get all the operations from the sql query
        sqlResult = [{sqlCursor.description[index][0]:column for index, column in enumerate(value)} for value in sqlCursor.fetchall()]
        for operation in sqlResult: # Rewrite datetime in specific format
            operation['datDate'] = operation['datDate'].strftime("%d/%m/%Y %H:%M:%S")

        return sqlResult, 200 # Return the JSON result

#######################################################################################################################
#######################################################################################################################
#### Rajout d'une opération
    def put(self, strAPI= ""):
        print(strAPI)
        args = operation_put_args.parse_args()
        print("Print ici:"+str(args))
        return {"Reponse":"NumeroInput= "+str(args["Numero"])}, 201

#######################################################################################################################
#######################################################################################################################
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

#######################################################################################################################
#######################################################################################################################
#### Suppression d'une opération
    def delete(self, intNumeroOperation):
        global ai_quotes
        ai_quotes = [qoute for qoute in ai_quotes if qoute["intNumeroOperation"] != intNumeroOperation]
        return f"Quote with id {intNumeroOperation} is deleted.", 200

#######################################################################################################################
#######################################################################################################################
#### Chemin de l'API (depuis: 54.37.9.75/)
api.add_resource(apiOperation, "/operation", "/operation/", "/operation/<string:strAPI>")

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()