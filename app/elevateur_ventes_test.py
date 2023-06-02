import unittest
from datetime import date
from burger import Burger
from elevateur_ventes import EvaluateurVentes

class EvaluateurVentesTests(unittest.TestCase):
    def setUp(self):
        # Crée une instance d'EvaluateurVentes pour chaque test
        self.evaluateur_ventes = EvaluateurVentes(date="2023-06-01")

    def test_evaluer_nombre_burgers_vendus(self):
        # Ajoute quelques burgers à l'evaluateur
        burger1 = Burger(prix=12.5, description="Burger 1", allergenes=[], cuisson="", scoville=0)
        burger2 = Burger(prix=15.0, description="Burger 2", allergenes =["glucose"], cuisson="saignant", scoville=0)
        self.evaluateur_ventes.ajouter_burger(burger1)
        self.evaluateur_ventes.ajouter_burger(burger2)

        # Vérifie le nombre de burgers vendus
        nombre_ventes = self.evaluateur_ventes.evaluer_nombre_burgers_vendus()
        self.assertEqual(nombre_ventes, 2)

    def test_evaluer_prix_total_ventes(self):
        # Ajoute quelques burgers à l'evaluateur
        burger1 = Burger(prix=12.5, description="Burger 1", allergenes=[], cuisson="", scoville=0)
        burger2 = Burger(prix=15.0, description="Burger 2", allergenes =["glucose"], cuisson="saignant", scoville=0)
        
        self.evaluateur_ventes.ajouter_burger(burger1)
        self.evaluateur_ventes.ajouter_burger(burger2)

        # Vérifie le prix total des ventes
        prix_total = self.evaluateur_ventes.evaluer_prix_total_ventes()
        self.assertEqual(prix_total, 27.5)

    def test_evaluer_allergenes_journee(self):
        # Ajoute quelques burgers à l'evaluateur avec des allergènes
        burger1 = Burger(prix=12.5, description="Burger 1", allergenes=["gluten"], cuisson="", scoville=0)
        burger2 = Burger(prix=15.0, description="Burger 2", allergenes=["gluten"], cuisson="", scoville=0)
        self.evaluateur_ventes.ajouter_burger(burger1)
        self.evaluateur_ventes.ajouter_burger(burger2)

        # Vérifie les allergènes présents dans la journée
        allergenes_journee = self.evaluateur_ventes.evaluer_allergenes_journee()
        self.assertEqual(allergenes_journee, ["gluten"])

if __name__ == '__main__':
    unittest.main()
