class Lien:
    """Lien du graphe"""

    __id = 0

    def __init__(self,noeud1,noeud2,distance):

        self.__noeud1 = noeud1
        self.__noeud2 = noeud2
        self.__distance = distance
        self.__id = Lien.__id

    def __str__(self):
        print(id)

    def getId(self):
        return self.__id

    def getNoeud1(self):
        return self.__noeud1

    def getNoeud2(self):
        return self.__noeud2

    def getDistance(self):
        return self.__distance

