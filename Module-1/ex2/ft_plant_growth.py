class Plant:
    """Represents a generic plant with basic growth attributes."""
    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Initializes plant information.

            Args:
                name (str): The name of the plant created.
                height (int): The height in cm of the plant created.
                current_age (int): The age in days of the plant created.
        """
        self.name = name
        self.height = height
        self.current_age = age

    def grow(self) -> None:
        """Increases plant height by 1 cm"""
        self.height += 1

    def age(self) -> None:
        """Increases the age of plants by 1 days"""
        self.current_age += 1

    def get_info(self) -> None:
        """
        Displays information about a plant on day 1 and day 7.
        And displays the overall change in its size.
        """
        print(f"{self.name}: {self.height}cm, {self.current_age} days old")


def ft_plant_growth() -> None:
    """
    create a plant using the Plant class,
    display it on day 1 and display it on day 7 with its growth over the week
    """
    plants = [
        Plant(name="Rose", height=25, age=30)
    ]
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
    days_passed = 6
    for _ in range(days_passed):
        for plant in plants:
            plant.grow()
            plant.age()
    print(f"=== Day {1 + days_passed} ===")
    for plant in plants:
        plant.get_info()
    print(f"Growth this week: +{days_passed}cm")


if __name__ == "__main__":
    ft_plant_growth()
