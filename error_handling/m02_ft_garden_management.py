#!/usr/bin/env python3

# ANSI
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

# combinations
BOLD_RED = BOLD + RED
BOLD_GREEN = BOLD + GREEN
BOLD_BLUE = BOLD + BLUE


class GardenError(Exception):
    """Base class for all garden-related errors"""
    pass


class PlantError(GardenError):
    """Raised when a plant has a problem"""
    pass


class WaterError(GardenError):
    """Raised when watering fails"""
    pass


class Plant:
    """A plant with attributes: name, height."""

    def __init__(self, name: str, height: int) -> None:
        """Create a new plant."""
        self.name = name.capitalize()
        self.height = height


class GardenManager:
    """Handles plants in the garden"""

    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        """Add plant to garden."""
        if not plant.name:
            raise PlantError("Plant name cannot be empty! ❌")
        self.plants.append(plant)
        print(f"- Added {plant.name} {GREEN}successfully{RESET}")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> None:
        """Check if plant is healthy"""

        if sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours}"
                             f" are too low (min 2) ❌")
        elif sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {sunlight_hours}"
                             f" are too high (max 12) ❌")
        if water_level < 1:
            raise PlantError(f"Water level {water_level}"
                             f" is too low (min 1) ❌")
        elif water_level > 10:
            raise PlantError(f"Water level {water_level}"
                             f" is too high (max 10) ❌")

        print(f"{plant_name}: {GREEN}healthy{RESET} "
              f"(water: {water_level}, sun: {sunlight_hours})")

    def water_plants(self, water_tank: int) -> None:
        """Open watering system, water each plant and close the system"""

        if water_tank < 1:
            raise WaterError("Not enough water in tank ❌")

        print("Opening watering system")

        try:
            for plant in self.plants:
                message = f"- Watering: {plant.name} - {GREEN}success{RESET}"
                print(message)
        except Exception:
            print(f"Error: Cannot water '{plant.name}' - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")


def test_garden_management() -> None:
    """Tests GardenManager functions and error handling"""

    print()
    print(f"{BOLD_BLUE}=== Garden Management System ==={RESET}")
    print()
    print("-------------------------------")

    garden = GardenManager()

    print(f"{BOLD}>> Adding plants to garden...{RESET}")
    print()

    tomato = Plant("tomato", 50)
    lettuce = Plant("lettuce", 20)
    invalid_plant = Plant("", 0)
    garden.add_plant(tomato)
    garden.add_plant(lettuce)
    try:
        garden.add_plant(invalid_plant)
    except PlantError as e:
        print(f"{RED}Error:{RESET} {e}")
    print()
    print("-------------------------------")

    print(f"{BOLD}>> Watering plants...{RESET}")
    print()

    garden.water_plants(10)
    print()
    print("-------------------------------")

    print(f"{BOLD}>> Checking plant health...{RESET}")
    print()

    garden.check_plant_health(tomato.name, 5, 8)
    try:
        garden.check_plant_health(lettuce.name, 15, 10)
    except GardenError as e:
        print(f"{RED}Error checking lettuce:{RESET} {e}")
    print()
    print("-------------------------------")

    print(f"{BOLD}>> Testing error recovery...{RESET}")
    print()

    try:
        garden.water_plants(0)
    except GardenError as e:
        print(f"{RED}Caught GardenError:{RESET} {e}")

    print("✅ System recovered and continuing...")
    print()
    print("-------------------------------")

    print(f"{BOLD_GREEN}Garden management system test complete!{RESET}")
    print()


if __name__ == "__main__":
    test_garden_management()
