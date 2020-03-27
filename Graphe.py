from noeud import Noeud
from lien import Lien

class Graphe:

    """Le graphe"""

    def __init__(self, id):

        self._id = id
        self._nbrNoeuds = 0
        self._dictNoeuds = []
        self._dictLiens = []

    def getNbrNoeuds(self):
        return self._nbrNoeuds

    def ajoutNoeud(self,Noeud):
        self._dictNoeuds.append(Noeud)

    def ajoutLien(self,Lien):
        self._dictLiens.append(Lien)
        Noeud.ajoutIdentifiantLien(Lien,Lien.getId())

    def ObtenirProchainNoeuds(self, idNoeud, dictId):
        return dictId = [Lien.getDistance(),]

