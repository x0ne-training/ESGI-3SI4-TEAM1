class Role:
    def __init__(self, name, description, team):
        self.name = name
        self.description = description
        self.team = team  # "village" ou "loup"

class LoupGarou(Role):
    def __init__(self):
        super().__init__("Loup-Garou", "Elimine un joueur chaque nuit", "loup")

class Voyante(Role):
    def __init__(self):
        super().__init__("Voyante", "Peut découvrir le rôle d'un joueur chaque nuit", "village")

class Villageois(Role):
    def __init__(self):
        super().__init__("Villageois", "N'a pas de pouvoir particulier", "village")
