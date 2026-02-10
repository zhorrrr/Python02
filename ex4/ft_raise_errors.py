def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None or plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 0 or water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is invalid (must be 1-10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is invalid (must be 2-12)")
    print(f"Plant {plant_name} is healthy ")

def ft_raise_errors():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("Rose", 1.5, 8)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 1.0, 6)
    except ValueError as error:
        print(f"Caught an error: {error}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("Tulip", -1.0, 6)
    except ValueError as error:
        print(f"Caught an error: {error}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Sunflower", 1.0, 0)
    except ValueError as error:
        print(f"Caught an error: {error}")
    print("\nAll error raising tests completed!")

if __name__ == "__main__":
    ft_raise_errors()