class Plant:
    """Represents a generic plant with basic growth attributes."""
    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Initializes plant information.

            Args:
                name (str): The name of the plant created.
                height (int): The height in cm of the plant created.
                age (int): The age in days of the plant created.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """One of the classes inheriting from Plant"""
    def __init__(self, *, name: str, height: int, age: int,
                 color: str) -> None:
        """Initializing Flower type variables using Plant

            Args:
                name (str): The name of the Flower created.
                height (int): The height in cm of the Flower created.
                age (int): The age in days of the Flower created.
                color (str): The color of the flower.
            """
        super().__init__(name=name, height=height, age=age)
        self.color = color

    def bloom(self) -> None:
        """Displays that the plant is blooming."""
        print(f"{self.name} is blooming beautifully!\n")

    def display_flower(self) -> None:
        """Displays information about the flower."""
        print(f"{self.name} (Flower): {self.height}cm,", end=" ")
        print(f"{self.age} days, {self.color} color")


class Tree(Plant):
    """One of the classes inheriting from Plant"""
    def __init__(self, *, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initializing Flower type variables using Plant

            Args:
                name (str): The name of the Flower created.
                height (int): The height in cm of the Flower created.
                age (int): The age in days of the Flower created.
                trunk_diameter (int): The diameter of the tree trunk.
            """
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Display the size in square meters of the tree's shade."""
        shade_square = int((self.height/100)**2 * 3.14159)
        print(f"{self.name} provides {shade_square} square meters of shade\n")

    def display_tree(self) -> None:
        """Displays information about the tree."""
        print(f"{self.name} (Tree): {self.height}cm,", end=" ")
        print(f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """One of the classes inheriting from Plant"""
    def __init__(self, *, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initializing Flower type variables using Plant

            Args:
                name (str): The name of the Flower created.
                height (int): The height in cm of the Flower created.
                age (int): The age in days of the Flower created.
                harvest_season (str): The vegetable harvest season.
                nutritional_value (str):The nutritional value of the vegetable.
            """
        super().__init__(name=name, height=height, age=age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_vegetable(self) -> None:
        """Displays information about the vegetable."""
        print(f"{self.name} (Vegetable): {self.height}cm,", end=" ")
        print(f"{self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is {self.nutritional_value}")


def ft_plant_types() -> None:
    """Create flowers, trees, and vegetables in the garden
    and posters with their characteristics."""
    print("=== Garden Plant Types ===\n")
    f_flower = Flower(name="Rose", height=25, age=30, color="red")
    f_flower.display_flower()
    f_flower.bloom()
    f_tree = Tree(name="Oak", height=500, age=1825, trunk_diameter=50)
    f_tree.display_tree()
    f_tree.produce_shade()
    f_vegetable = Vegetable(name="Tomato", height=80, age=90,
                            harvest_season="summer",
                            nutritional_value="rich in vitamin C")
    f_vegetable.display_vegetable()


if (__name__ == "__main__"):
    ft_plant_types()
