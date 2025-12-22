class SecurePlant:
    """Represents a generic plant with basic growth attributes."""
    def __init__(self, *, name: str, height: int, age: int) -> None:
        """Initializes plant information.

            Args:
                name (str): The name of the plant created.
                __height (int): The height in cm of the plant created.
                __age (int): The age in days of the plant created.
        """
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant created: {self.name}")

    def get_height(self) -> int:
        """Getter that allows you to obtain the size of the plant."""
        return self.__height

    def set_height(self, *, height: int) -> None:
        """
        Setter that allows you to set the height of the plant.
        Also check if the new height has a possible value.

        Height (int): Variable corresponding to the new height of the plant.
        """
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print("\nInvalid operation attempted: height "
                  f"{height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print(f"Current plant: {self.name} ({self.__height}cm, "
                  f"{self.__age} days)")

    def get_age(self) -> int:
        """Getter that allows you to obtain the size of the plant."""
        return self.__age

    def set_age(self, *, age: int) -> None:
        """
        Setter that allows you to set the age of the plant.
        Also check if the new age has a possible value.

        Age (int): Variable corresponding to the new age of the plant.
        """
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            print(f"Current plant: {self.name} ({self.__height}cm, "
                  f"{self.__age} days)")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant(name="Rose", height=24, age=29)
    plant.set_height(height=30)
    plant.set_age(age=25)
    plant.set_height(height=-5)


if __name__ == "__main__":
    ft_garden_security()
