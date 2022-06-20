class clsOperation: #Classe d'une opération
    def __init__(self,operation):
        self.intNumero = operation["intNumero"] #Numero de l'operation
        self.datDate = operation["datDate"] #Date de l'opération
        self.strType = operation["strType"] #Type de l'operation (Achat,RachatDividende,Dividende,Vente)
        self.intNombre = operation["intNombre"] #Nombre de titre concerné
        self.douMontant = operation["douMontant"] #Montant de l'opération
        self.strCommentaire = operation["strCommentaire"] #Commentaire éventuel concernant cette opération
