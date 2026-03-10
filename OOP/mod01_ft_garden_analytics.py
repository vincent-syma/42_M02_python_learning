#!/usr/bin/env python3

class Plant:
    """A plant with attributes: name, height + grow ability."""

    def __init__(self, name: str, height: int) -> None:
        """Create a new plant."""
        self.name = name.capitalize()
        self._height = height
        self.growth = 0

    def plant_type(self) -> str:
        return "regular"

    def set_height(self, value: int) -> bool:
        """Safely update height."""
        if value < 0:
            return False
        self._height = value
        return True

    def get_height(self) -> int:
        """Return current height."""
        return self._height

    def grow(self) -> None:
        """Increase plant height by 1 cm."""
        self._height += 1
        self.growth += 1

    def get_info(self) -> str:
        """Return plant summary as string."""
        return f"{self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
    """Flower plant with color and bloom ability."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Create a new flower plant and call parent constructor."""
        super().__init__(name, height)
        self.color = color

    def plant_type(self) -> str:
        return "flowering"

    def bloom(self) -> str:
        """Returns that flower is blooming as a string."""
        return "blooming"

    def get_info(self) -> str:
        """Return flower summary as string."""
        base_info = super().get_info()
        return f"{base_info}, {self.color} flowers ({self.bloom()})"


class PrizeFlower(FloweringPlant):
    """Flower plant with color and bloom ability."""

    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        """Create a new prize flower plant and call parent constructor."""
        super().__init__(name, height, color)
        self.points = points

    def plant_type(self) -> str:
        return "prize"

    def get_info(self) -> str:
        """Return prize flower summary as string."""
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.points}"


class Garden:
    """One garden containing plants."""

    def __init__(self, owner: str) -> None:
        """Create a new garden."""
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        """Add plant to garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self) -> None:
        """Add every plant in garden."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def report(self) -> None:
        """Print garden statistics."""
        print(f"=== {self.owner}'s Garden Report ===")
        print()

        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print()

        plants_total = GardenManager.GardenStats.count_plants(self.plants)
        growth_total = GardenManager.GardenStats.total_growth(self.plants)

        print(f"Plants added: {plants_total}, Total growth: {growth_total}cm")

        regular, flowering, prize = (
            GardenManager.GardenStats.count_types(self.plants))

        print(f"Plant types: {regular} regular, {flowering} flowering, "
              f"{prize} prize flowers")
        print()
        print("=== END ===")
        print()


class GardenManager:
    """Handles multiple gardens."""

    gardens = []

    @classmethod
    def create_garden_network(cls):
        """Initialize garden network."""
        cls.gardens = []
        print("Garden network created.")

    @classmethod
    def add_garden(cls, garden: Garden) -> None:
        cls.gardens.append(garden)
        print(f"{garden.owner}'s garden added to the network.")

    @classmethod
    def report(cls) -> None:
        """Print garden network statistics."""
        print("=== Garden Network Report ===")
        print()

        total_gardens = 0
        for _ in cls.gardens:
            total_gardens += 1

        scores = "Garden scores - "
        for garden in cls.gardens:
            points = cls.GardenStats.count_points(garden.plants)

            scores += f"{garden.owner}: {points} points, "

        print(scores[:-2])
        print(f"Total gardens managed: {total_gardens}")
        print()
        print("=== END ===")
        print()

    class GardenStats:
        """Helper for calculating statistics."""

        @staticmethod
        def count_plants(plants: list) -> int:
            """Counts plants (manually)."""
            count = 0
            for _ in plants:
                count += 1
            return count

        @staticmethod
        def total_growth(plants: list) -> int:
            """Calculates total height of all plants."""
            total = 0
            for plant in plants:
                total += plant.growth
            return total

        @staticmethod
        def count_types(plants: list) -> tuple:
            regular = 0
            flowering = 0
            prize = 0

            for plant in plants:
                ptype = plant.plant_type()

                if ptype == "regular":
                    regular += 1
                elif ptype == "flowering":
                    flowering += 1
                elif ptype == "prize":
                    prize += 1

            return regular, flowering, prize

        @staticmethod
        def count_points(plants: list) -> int:
            points = 0

            for plant in plants:
                type = plant.plant_type()

                if type == "prize":
                    points += plant.points

            return points


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    GardenManager.create_garden_network()

    alice_garden = Garden("Alice")
    GardenManager.add_garden(alice_garden)
    print()

    alice_garden.add_plant(Plant("Oak Tree", 500))
    alice_garden.add_plant(FloweringPlant("Rose", 50, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 100, "yellow", 10))
    print()

    alice_garden.grow_all_plants()
    print()

    bob_garden = GardenManager.add_garden(Garden("Bob"))
    print()

    alice_garden.report()

    test_plant = Plant("Validator", 10)
    valid = test_plant.set_height(15)
    invalid = test_plant.set_height(-5)
    print(f"Height validation test: {valid and not invalid}")
    print()

    GardenManager.report()
