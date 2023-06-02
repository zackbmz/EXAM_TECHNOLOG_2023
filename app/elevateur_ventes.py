class EvaluateurVentes:
    def __init__(self, date):
        self.date = date
        self.burgers = []

    def ajouter_burger(self, burger):
        self.burgers.append(burger)

    def evaluer_nombre_burgers_vendus(self):
        return len(self.burgers)

    def evaluer_prix_total_ventes(self):
        return sum(burger.prix for burger in self.burgers)

    def evaluer_allergenes_journee(self):
        allergenes = set()
        for burger in self.burgers:
            allergenes.update(burger.allergenes)
        return list(allergenes)
