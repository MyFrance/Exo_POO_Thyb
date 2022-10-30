class Voiture: 
    def __init__(self, marque, couleur):
        self.marque = "Mazda"
        self.couleur = "Rouge"

    def recuperer_couleur(self, couleur):
        self.couleur = couleur
        return couleur
    
mazda_rouge = Voiture("Mazda", "Rouge")
mazda_rouge.recuperer_couleur(couleur="rouge")
print(mazda_rouge.couleur)