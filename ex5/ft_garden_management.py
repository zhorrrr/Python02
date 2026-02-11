class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

class GardenManager:
    def __init__(self) -> None:
        self.plants = []
    
    def add_plant(self, name : str, water_level : int, sunlight_hours : int) -> None:
        if name is None or name == "":
            raise PlantError("Plant name cannot be empty!")
        
        try:
            if water_level < 1 or water_level > 10:
                raise PlantError(f"Water level {water_level} is too high (max 10)")
        except TypeError:
            raise PlantError("Water level must be a number!")
        
        try:
            if sunlight_hours < 2 or sunlight_hours > 12:
                raise PlantError(f"Sunlight hours {sunlight_hours} is invalid (must be 2-12)")
        except TypeError:
            raise PlantError("Sunlight hours must be a number!")
        
        plant = Plant(name, water_level, sunlight_hours)
        self.plants = self.plants + [plant]
        print(f"Added {name} successfully")
    
    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")
    
    def check_plant_health(self, plant_name : str) -> None:
        if plant_name is None or plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        
        plant = None
        for p in self.plants:
            if p.name == plant_name:
                plant = p
                break
        
        if plant is None:
            raise PlantError(f"Plant '{plant_name}' not found in garden")
        
        if plant.water_level < 1 or plant.water_level > 10:
            raise PlantError(f"Water level {plant.water_level} is too high (max 10)")
        
        if plant.sunlight_hours < 2 or plant.sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {plant.sunlight_hours} is invalid (must be 2-12)")
        
        print(f"{plant_name}: healthy (water: {plant.water_level}, sun: {plant.sunlight_hours})")

def test_garden_management():
    print("=== Garden Management System ===\n")
    
    garden = GardenManager()
    
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 6, 7)
        garden.add_plant("", 5, 6)
    except PlantError as error:
        print(f"Error adding plant: {error}")
    
    print("\nWatering plants...")
    garden.water_plants()
    
    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato")
        for plant in garden.plants:
            if plant.name == "lettuce":
                plant.water_level = 15
        garden.check_plant_health("lettuce")
    except PlantError as error:
        print(f"Error checking lettuce: {error}")
    
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")
    
    print("\nGarden management system test complete!")

if __name__ == "__main__":
    test_garden_management()
