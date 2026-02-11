class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def check_plant(plant: str) -> None:
    if plant == "":
        raise PlantError("Plant name cannot be empty!")
    print(f"Plant '{plant}' is healthy!")

def check_water(water_amount: int) -> None:
    if water_amount < 0:
        raise WaterError("Water amount cannot be negative!")
    print(f"Water amount {water_amount}ml is sufficient!")

def test_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant("")
    except PlantError:
        print("Caught PlantError: Plant name cannot be empty!\n")
    

    print("Testing WaterError...")
    try:
        check_water(-5)
    except WaterError:
        print("Caught WaterError: Water amount cannot be negative!\n")
    
    print("\nTesting catching all garden errors...")
    try:
        check_plant("")
    except GardenError:
        print("Caught PlantError via GardenError parent!\n")

def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_errors()
    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    ft_custom_errors()