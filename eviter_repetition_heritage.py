class Personnage: 
    def __init__(self, prenom, nom, puissance):
        self.prenom = prenom
        self.nom = nom
        self.puissance = puissance
    def afficher(self):
        print(f"{self.prenom} {self.nom} puissance {self.puissance} ")

class Magicien(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom, puissance=80)
        
        
class Gobelin(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom, puissance=20)
        

class Chevalliers(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom, puissance=70)
        

personnages= Magicien("Gandalf", "Legris")
personnages.afficher()

