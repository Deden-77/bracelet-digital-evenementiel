# Masse volumique de l'ethanol (=l'alcool) : 790 g/L
#                                        ou 0,79 g/mL
MASSE_VOLUMIQUE_ETHANOL = 790 # g/L


class Buyable():
    def __init__(self) -> None:
        self.price: int = 100 # IN CENTIMES, so 1000 = 10€.


class Drink(Buyable):
    def __init__(self, name: str, alcohol_degree: float, volume: int) -> None:
        super().__init__()
        self.name = name
        self.alcohol_degree = alcohol_degree # x% Vol. (proportion d'alcool dans la boisson, sous forme de Pourcentage du volume (par exemple 0.05 (5%) environ pour la bière)). Autrement dit, c'est le volume d'alcool par rapport au volume total de liquide
        self.volume = volume # In mililitre
    
    @property
    def alcohol_volume(self) -> int: # En mililitre
        return int(self.volume * self.alcohol_degree)
    
    @property
    def contains_alcohol(self) -> bool:
        return self.alcohol_degree != 0
    
    @property
    def alcohol_mass(self) -> float: # En grammes
        return MASSE_VOLUMIQUE_ETHANOL/1000 * self.alcohol_volume
    
    @property
    def alcohol_unit(self) -> float: # Voir https://fr.wikipedia.org/wiki/Unit%C3%A9_d%27alcool et https://en.wikipedia.org/wiki/Standard_drink
        return self.alcohol_mass / 10


class Food(Buyable):
    def __init__(self, name: str, calories: int = None) -> None:
        super().__init__()
        self.name = name
        # A word about calories:  1 kcal = 1 Cal  <=>  1000 cal = 1000 calories
        # self.kcalories: int
        self._calories = calories
        self._kcalories = calories/1000

    @property
    def calories(self) -> int:
        return self._calories
    
    @calories.setter
    def calories(self, value: int): # Called when setting the .calories attribute
        self._calories = value
    
    @property
    def kcalories(self) -> float:
        return self._calories / 1000
    
    @kcalories.setter
    def kcalories(self, value: float):
        self._calories = int(value*1000)


thor = Drink(
    name="Thor",
    alcohol_degree=0.05,
    volume=500
)
print("Thor:", thor.alcohol_unit, "unités")


wine_test = Drink(
    name="Wine test",
    alcohol_degree=0.12,
    volume=750
)
print("Wine test:", round(wine_test.alcohol_unit, 2), "unités")