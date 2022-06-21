import datetime
import json

def defaultJSON(value):
    if isinstance(value, datetime.date):
        return value.strftime("%d/%m/%Y %H:%M:%S")
    return value.__dict__


class clsOperation: #Classe d'une opération

    def __init__(self, operation):
        self.intNumero = operation[0] #Numero de l'operation
        self.datDate = operation[1] #Date de l'opération
        self.strType = operation[2] #Type de l'operation (Achat,RachatDividende,Dividende,Vente)
        self.intNombre = operation[3] #Nombre de titre concerné
        self.douMontant = operation[4] #Montant de l'opération
        self.strCommentaire = operation[5] #Commentaire éventuel concernant cette opération
        self.booIgnore = operation[6] #Commentaire éventuel concernant cette opération

    def getJSON(self): # Return JSON of this operations
        return json.dumps(self, default = defaultJSON)

    # def __init__(self,operation):
    #     self.intNumero = operation["intNumero"] #Numero de l'operation
    #     self.datDate = operation["datDate"] #Date de l'opération
    #     self.strType = operation["strType"] #Type de l'operation (Achat,RachatDividende,Dividende,Vente)
    #     self.intNombre = operation["intNombre"] #Nombre de titre concerné
    #     self.douMontant = operation["douMontant"] #Montant de l'opération
    #     self.strCommentaire = operation["strCommentaire"] #Commentaire éventuel concernant cette opération
    #     self.booIgnore = operation["booIgnore"] #Commentaire éventuel concernant cette opération
