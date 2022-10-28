class Employe: 
    def __init__(self, prenom, nom, position,salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire

    def afficher_employer(self):
        print(f"Je m'appelle {self.prenom} {self.nom} j'occupe le poste de {self.position} et je gagne {self.salaire} €")

francois =Employe("François", "Dupont", "Développeur", 4500)
Employe.afficher_employer(francois)
