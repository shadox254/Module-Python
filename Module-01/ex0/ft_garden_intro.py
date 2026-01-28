def ft_garden_intro() -> None:
    """Initializes plant information and displays it.

        Args:
            name (str): The name of the plant created.
            height (int): The height in cm of the plant created.
            age (int): The age in days of the plant created.
    """
    name = str("Rose")
    height = int(25)
    age = int(30)

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===")


if (__name__ == "__main__"):
    ft_garden_intro()
