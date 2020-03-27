class Noeud:

    """Les Noeuds du graphe"""

    id = 0

    def __init__(self,listId, id):
        self.__listId = list(listId)
        self.id = id
        Noeud.id+=1

    def __str__(self):
        return Noeud.id

    def affichageIdentifiantLien(self):
        print(self.__listId)

    def ajoutIdentifiantLien(self, id):
        self.__listId.append(id)

    def renvoieIdentifiantLien(self):
        return self.id
