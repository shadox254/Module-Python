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

    def display_infos(self) -> None:
        """Displays information about a plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """create plants with the Plant class and display them

        Args:
            rose (Plant): The plant named “rose” of type Plant with its
                characteristics.
            sunflower (Plant): The plant named "sunflower” of type Plant with
                its characteristics.
            cactus (Plant): The plant named "cactus” of type Plant with its
                characteristics.
    """
    plant_list = [
        Plant(name="Rose", height=25, age=30),
        Plant(name="Sunflower", height=80, age=45),
        Plant(name="Cactus", height=15, age=120)
    ]
    print("=== Garden Plant Registry ===")
    for plants in plant_list:
        plants.display_infos()


if (__name__ == "__main__"):
    ft_garden_data()
