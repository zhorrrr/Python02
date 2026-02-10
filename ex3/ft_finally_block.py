def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)\n")

def ft_finally_block():
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    
    print("Testing with error...")
    water_plants(["tomato", None, "daisy"])
    
    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    ft_finally_block()
