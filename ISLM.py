import matplotlib.pyplot as plt
import numpy as np

class IS_LM_Model:
    def __init__(self, c0, c1, I0, I1, G, T, M, P, alpha, beta, gamma):
        self.c0 = c0  # Consommation autonome
        self.c1 = c1  # Propension marginale à consommer
        self.I0 = I0  # Investissement autonome
        self.I1 = I1  # Sensibilité de l'investissement au taux d'intérêt
        self.G = G    # Dépenses publiques
        self.T = T    # Impôts
        self.M = M    # Offre monétaire
        self.P = P    # Niveau des prix
        self.alpha = alpha  # Sensibilité de la demande de monnaie au revenu
        self.beta = beta    # Sensibilité de la demande de monnaie au taux d'intérêt
        self.gamma = gamma  # Sensibilité de la demande d'investissement au taux d'intérêt

    def calcule_IS(self, Y, r):
        return (self.c0 + self.c1*(Y - self.T) + self.I0 - self.I1*r + self.G)

    def calcule_LM(self, Y, r):
        return (self.M/self.P) * (self.alpha * Y - self.beta * r)

    def affiche_IS_LM(self):
        Y = np.linspace(0, 500, 100)
        r = np.linspace(0, 0.2, 100)

        IS_curve = self.calcule_IS(Y, 0)
        LM_curve = self.calcule_LM(Y, 0)

        plt.plot(Y, IS_curve, label='IS curve')
        plt.plot(Y, LM_curve, label='LM curve')
        plt.xlabel('Output (Y)')
        plt.ylabel('Interest Rate (r)')
        plt.title('IS-LM Model')
        plt.legend()
        plt.grid(True)
        plt.show()

# Exemple d'utilisation
modele = IS_LM_Model(c0=50, c1=0.8, I0=100, I1=50, G=150, T=100, M=500, P=1, alpha=0.01, beta=1, gamma=1)
modele.affiche_IS_LM()

print(modele.calcule_LM(10, 10))