class Equipe:
    instances = []

    def __init__(self, nom, point=1, poule="A"):
        self.nom = nom
        self.joueurs = []
        self.poule = poule
        self.point = point
        self.staf = []
        Equipe.instances.append(self)

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def supprimer_joueur(self, joueur):
        self.joueurs.remove(joueur)

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def supprimer(self):
        Equipe.instances.remove(self)

    def get_joueur(self):
        return [joueur for joueur in self.joueurs]

    def get_point(self):
        return self.point

    def get_poule(self):
        return self.poule

    # @classmethod
    # def creer_equipe(cls, nom):
    #     return cls(nom)

    @classmethod
    def lister_equipes(cls):
        return [equipe.nom for equipe in cls.instances]

    @classmethod
    def trouver_equipe_by_index(cls,index):
        for equipe in cls.instances:
            if cls.instances.index(equipe) == index:
                return equipe
        return None

    @classmethod
    def trouver_equipe(cls, nom):
        for equipe in cls.instances:
            if equipe.nom == nom:
                return equipe
        return None
