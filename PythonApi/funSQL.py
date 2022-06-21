

function getOperation(intNumeroOperation):
    if intNumeroOperation == -1:
#### Récupération du numero de la dernière opération de la table
        sqlRequete = 'SELECT * FROM lisOperations ORDER BY intNumero DESC LIMIT 1;'
    else:
#### Récupération du numero de la dernière opération de la table
        sqlRequete = 'SELECT * FROM lisOperations WHERE intNumero = '+ str(intNumeroOperation) +';'

    sqlCursor.execute(sqlRequete)
    sqlResponse = sqlCursor.fetchall()
    print(sqlResponse)

    return sqlResponse