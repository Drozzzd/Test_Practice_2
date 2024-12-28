# (Д)дроздов -> (Д)драники

class Ingredient:
    """Ингредиент."""

    def __init__(self, name, raw_weight, cooked_weight, cost) -> None:
        self.name = name
        self.raw_weight = raw_weight
        self.cooked_weight = cooked_weight
        self.cost = cost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Название ингредиента должно быть строкой")
        self._name = value

    @property
    def raw_weight(self):
        return self._raw_weight

    @raw_weight.setter
    def raw_weight(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Вес сырого продукта должен быть положительным числом")
        self._raw_weight = value

    @property
    def cooked_weight(self):
        return self._cooked_weight

    @cooked_weight.setter
    def cooked_weight(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Вес готового продукта должен быть положительным числом")
        self._cooked_weight = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Себестоимость должна быть положительным числом")
        self._cost = value

    def __str__(self) -> str:
        return f"{self.name} (raw: {self.raw_weight}g, cooked: {self.cooked_weight}g, cost: {self.cost} rub)"