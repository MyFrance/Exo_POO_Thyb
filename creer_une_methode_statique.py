class Chanson:
   
    paroles = """Joyeux anniversaire,
Joyeux anniversaire,
Joyeux anniversaire {prenom},
Joyeux anniversaire."""
        

    @staticmethod
    def chante_pour(prenom):
        return Chanson.paroles.format(prenom=prenom)

paul = Chanson()
print(Chanson.chante_pour("Paul"))
