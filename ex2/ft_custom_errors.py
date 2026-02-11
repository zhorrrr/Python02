class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def check_plant(plant: str) -> None:
    if plant == "wilting":
        raise PlantError("The tomato plant is wilting!")
    print(f"Plant '{plant}' is healthy!")

def check_water(water_amount : int) -> None:
    if water_amount < 10:
        raise WaterError("Not enough water in the tank!")
    print(f"Water amount {water_amount}ml is sufficient!")

def test_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant("wilting")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    
    print("\nTesting WaterError...")
    try:
        check_water(5)
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    
    print("\nTesting catching all garden errors...")
    try:
        check_plant("wilting")
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    
    try:
        check_water(5)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    test_errors()
    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    ft_custom_errors()