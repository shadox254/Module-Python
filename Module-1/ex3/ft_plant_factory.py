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
        print(f"{self.name} ({self.height}cm, {self.age} days)")


def ft_garden_data() -> None:
    """Create plants and display them one by one,
    showing the number of plants created at the end.

        Args:
            count (int): The number of plants created.
            plant_list (lst): The list of all plants created.
    """
    count = 0
    plant_list = [
        Plant(name="Rose", height=25, age=30),
        Plant(name="Oak", height=200, age=365),
        Plant(name="Cactus", height=5, age=90),
        Plant(name="Sunflower", height=80, age=45),
        Plant(name="Fern", height=15, age=120)
    ]
    print("=== Plant Factory Output ===")
    for plants in plant_list:
        print("Created:", end=" ")
        plants.display_infos()
        count += 1
    print(f"\nTotal plants created: {count}")


if (__name__ == "__main__"):
    ft_garden_data()
