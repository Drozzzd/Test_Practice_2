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


class Receipt:
    """Рецепт."""

    def __init__(self, name: str, ingredient_list: list[tuple[str, int, int, int]]) -> None:
        self.name = name
        self.ingredients = [Ingredient(*ingredient) for ingredient in ingredient_list]

    def calc_cost(self, portions=1):
        total_cost = sum(ingredient.cost * portions for ingredient in self.ingredients)
        return total_cost

    def calc_weight(self, portions=1, raw=True):
        if raw:
            total_weight = sum(ingredient.raw_weight * portions for ingredient in self.ingredients)
        else:
            total_weight = sum(ingredient.cooked_weight * portions for ingredient in self.ingredients)
        return total_weight

    def __str__(self) -> str:
        ingredients_str = "\n".join(str(ingredient) for ingredient in self.ingredients)
        return f"Receipt: {self.name}\nIngredients:\n{ingredients_str}"


if __name__ == '__main__':
    receipt_from_api = {
        "title": "Драники",
        "ingredients_list": [
            ('Картофель', 500, 400, 50),
            ('Лук', 100, 80, 20),
            ('Яйцо', 50, 40, 10),
            ('Соль', 5, 5, 2),
            ('Масло подсолнечное', 50, 40, 30),
        ],
    }

    receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])

    # Самопроверка
    print(receipt)
    print(f"Себестоимость: {receipt.calc_cost()} руб.")
    print(f"Вес сырого продукта: {receipt.calc_weight(raw=True)} г")
    print(f"Вес готового продукта: {receipt.calc_weight(raw=False)} г")