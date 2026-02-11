def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    if plant_name is None or plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    
    try:
        if water_level < 0 or water_level > 10:
            raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    except TypeError:
        raise ValueError("Error: Water level must be a number!")
    
    try:
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    except TypeError:
        raise ValueError("Error: Sunlight hours must be a number!")
    
    print(f"Plant '{plant_name}' is healthy!")

def ft_raise_errors() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 5, 8)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as error:
        print(error)
    print("\nTesting bad water level...")
    try:
        check_plant_health("Tulip", 15, 6)
    except ValueError as error:
        print(error)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Sunflower", 5, 0)
    except ValueError as error:
        print(error)
    print("\nAll error raising tests completed!")

if __name__ == "__main__":
    ft_raise_errors()