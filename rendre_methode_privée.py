class MachineACafe: 
    def __init__(self):
        self.temperature_eau = 0

# Méthode privée
    def __chauffe_eau (self):
        self.temperature_eau = 100
        print("L'eau est chaude")
        
#Méthode privée
    def __moud_cafe(self):
        print("Café moulu avec succès")

    def fait_du_cafe(self):
        self.__chauffe_eau()
        self.__moud_cafe()
        print("Le café est prêt")

machine = MachineACafe()
machine.fait_du_cafe()