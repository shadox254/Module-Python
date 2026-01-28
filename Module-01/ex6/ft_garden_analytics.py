class GardenManager:
    """Manage multiples gardens."""
    total_gardens = 0

    def __init__(self) -> None:
        """The initialization of the garden.

            Args:
                gardens (dict): A dictionary that contains
                 every personal garden.
        """
        self.gardens = {}

    class GardenStats:
        """All garden statistics.

            Args:
                total_plant (int): The total number of all plants of all class
                 in the garden.
                regular (int): The total of all plants in the class Plant.
                flowering (int): The total of all plants in the
                 class FloweringPlant.
                prize_flower (int): The total of all plants in the
                 class PrizeFlower.
        """
        total_plant = 0
        regular = 0
        flowering = 0
        prize_flower = 0

    def add_plant(self, *, owner, plant) -> None:
        """Added a plant to a garden.

            Args:
                owner (str): The garden where we are going to add the plant.
                plant (Plant, FloweringPlant or PrizePlant): the plant added
                 to the owner's garden.
        """
        if owner not in self.gardens:
            print(f"Garden {owner} not exist")
            return
        self.gardens[owner]["plants"].append(plant)
        GardenManager.GardenStats.total_plant += 1
        if isinstance(plant, PrizeFlower):
            GardenManager.GardenStats.prize_flower += 1
            self.gardens[owner]["score"].append(plant.height)
            self.gardens[owner]["score"].append(plant.prize_p)
        elif isinstance(plant, FloweringPlant):
            GardenManager.GardenStats.flowering += 1
            self.gardens[owner]["score"].append(plant.height)
        elif isinstance(plant, Plant):
            GardenManager.GardenStats.regular += 1
            self.gardens[owner]["score"].append(plant.height)
        self.gardens[owner]["score"].append(10)
        print(f"Added {plant.name} to {owner}'s garden")

    @classmethod
    def create_garden_network(cls, owner_names) -> dict:
        """Create garden with in it each owner of garden.

            Args:
                owner_names (lst): list of all owner of gardens.

            Return: Return a dictionary with all owners and their gardens.
        """
        manager = cls()
        for owner in owner_names:
            if owner in manager.gardens:
                print(f"{owner}'s garden already exists.")
                continue
            manager.gardens[owner] = {
                "plants": [],
                "score": [],
                "growth": 0
            }
            GardenManager.total_gardens += 1
        return manager

    def grow_plants(self, *, owner) -> None:
        """
            Use method grow of Plant class on each plants of the garden
            of owner.

            Args:
                owner (str): The owner of the garden.
        """
        print(f"{owner} is helping all plants grow...")
        for plants in self.gardens[owner]["plants"]:
            plants.grow(size=1)
            self.gardens[owner]["growth"] += 1

    def get_score(self, *, owner) -> int:
        """Calculate the scores for each garden.

            Args:
                owner (str): The owner of the garden.

            Return: Return the score of the garden.
        """
        score = 0
        plant_lists = self.gardens[owner]["plants"]
        for plants in plant_lists:
            score += plants.height + 10
            if isinstance(plants, PrizeFlower):
                score += plants.prize_p
        return score

    @staticmethod
    def validate_height(all_gardens) -> bool:
        """"Check if the height is valid ( > 0) in all gardens.

            Args:
                all_gardens (dict): dictionary of all my gardens.

            Return: True if all heights are valid or False.
        """
        for owner in all_gardens:
            plants_lists = all_gardens[owner]["plants"]
            for plant in plants_lists:
                if plant.height < 0:
                    return False
        return True

    def print_garden_report(self) -> None:
        """Print the garden report."""
        scores_list = []
        for owner in self.gardens:
            if not self.gardens[owner]["plants"]:
                continue
            cnt_regular = 0
            cnt_flowering = 0
            cnt_prize = 0
            cnt_total = 0
            print(f"\n=== {owner}'s Garden Report ===")
            info = "Plants in garden:"
            plant_garden = self.gardens[owner]["plants"]
            for plant in plant_garden:
                info += f"\n{plant.get_plant_info()}"
                cnt_total += 1
                if isinstance(plant, PrizeFlower):
                    cnt_prize += 1
                elif isinstance(plant, FloweringPlant):
                    cnt_flowering += 1
                elif isinstance(plant, Plant):
                    cnt_regular += 1
            print(info)

            stats = f"\nPlants added: {cnt_total}, "
            stats += f"Total growth: {self.gardens[owner]['growth']}cm"
            stats += f"\nPlant types: {cnt_regular} regular, "
            stats += f"{cnt_flowering} flowering, "
            stats += f"{cnt_prize} prize flowers"
            print(stats)

            current_score = self.get_score(owner=owner)
            scores_list.append(f"{owner}: {current_score}")

        validate_height = self.validate_height(self.gardens)
        print(f"\nHeight validation test: {validate_height}")
        print(f"Garden scores - {', '.join(scores_list)}")
        print(f"Total gardens managed: {GardenManager.total_gardens}")


class Plant:
    """Represents a generic plant with basic attributes."""
    def __init__(self, *, name, height) -> None:
        """Initializes plant information.

            Args:
                name (str): The name of the plant created.
                height (int): The height in cm of the plant created.
                age (int): The age in days of the plant created.
        """
        self.name = name
        self.height = height

    def grow(self, *, size) -> None:
        """Grow the plant of the specified size.

            Args:
                size (int): the size of the plant we want to add.
        """
        self.height += size
        print(f"{self.name} grew {size}cm")

    def get_plant_info(self) -> str:
        """Display plant infos

            Return: Return a string with information about the plant
        """
        info = f"- {self.name}: {self.height}cm"
        return info


class FloweringPlant(Plant):
    """
    Represents a generic flower with basic attributes.
    It is a class that inherits from Plant.
    """
    def __init__(self, *, name, height, color) -> None:
        """Initializing FloweringPlant type variables using Plant

        name (str): The name of the Flower created.
        height (int): The height in cm of the Flower created.
        color (str): The color of the flower.
        """
        super().__init__(name=name, height=height)
        self.color = color

    def get_plant_info(self) -> str:
        """Display plant infos

            Return: Return a string with information about the plant
        """
        info = f"- {self.name}: {self.height}cm, {self.color} "
        "flowers (blooming)"
        return info


class PrizeFlower(FloweringPlant):
    """
    Represents a generic flower with basic attributes.
    It is a class that inherits from FloweringPlant.
    """
    def __init__(self, *, name, height, color, prize_points) -> None:
        """Initializing PrizeFlower type variables using FloweringPlant

        name (str): The name of the Flower created.
        height (int): The height in cm of the Flower created.
        color (str): The color of the flower.
        prize_points (int): The prize of the flower.
        """
        super().__init__(name=name, height=height, color=color)
        self.prize_p = prize_points

    def get_plant_info(self) -> str:
        """Display plant infos

            Return: Return a string with information about the plant
        """
        info = f"- {self.name}: {self.height}cm, {self.color}"
        f"flowers (blooming), Prize points: {self.prize_p}"
        return info


def ft_garden_analytics():
    """Main function for managing multiple gardens, adding plants to them,
    displaying them, and growing the plants."""
    oak = Plant(name="Oak Tree", height=100)
    rose = FloweringPlant(name="Rose", height=25, color="red")
    sunflower = PrizeFlower(name="Sunflower", height=50, color="yellow",
                            prize_points=10)
    birch = Plant(name="Birch Tree", height=52)
    passionflower = PrizeFlower(name="Passionflower", height=15, color="white",
                                prize_points=5)
    names = ["Alice", "Bob"]
    manager = GardenManager.create_garden_network(names)
    print("=== Garden Management System Demo ===\n")
    manager.add_plant(owner="Alice", plant=oak)
    manager.add_plant(owner="Alice", plant=rose)
    manager.add_plant(owner="Alice", plant=sunflower)
    manager.add_plant(owner="Bob", plant=birch)
    manager.add_plant(owner="Bob", plant=passionflower)
    print()
    manager.grow_plants(owner="Alice")
    manager.print_garden_report()


if (__name__ == "__main__"):
    ft_garden_analytics()
