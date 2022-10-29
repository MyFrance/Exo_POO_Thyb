class Livre:
    prix = 9.99
    def __init__(self, prix):
        self.prix = prix

    def changer_prix(self, prix): 
        self.prix = prix
        print(prix)

harry_poter = Livre(19.99)
print(harry_poter.prix)
harry_poter.changer_prix(prix = 14.99)

        