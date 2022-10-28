class Livre: 
    prix = 9.99
    def __init__(self, prix):
        self.prix = prix

    def Afficher_prix(self):
        print(f"Le livre coûte {self.prix} €")

harry_potter = Livre(19.99)

Livre.Afficher_prix(harry_potter)