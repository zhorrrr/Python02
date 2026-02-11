from typing import List

class GardenError(Exception):
    pass

class InvalidPlantError(GardenError):
    pass

class WaterTankError(GardenError):
    pass

class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int) -> None:
        self.name: str = name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours

class GardenManager:
    def __init__(self) -> None:
        self.plants: List[Plant] = []
        self.water_tank: int = 100
    
    def validate_water_level(self, water_level: int) -> None:
        try:
            if water_level < 1 or water_level > 10:
                raise InvalidPlantError(f"Water level {water_level} is invalid (must be 1-10)")
        except TypeError:
            raise InvalidPlantError("Water level must be a number!")
    
    def validate_sunlight_hours(self, sunlight_hours: int) -> None:
        try:
            if sunlight_hours < 2 or sunlight_hours > 12:
                raise InvalidPlantError(f"Sunlight hours {sunlight_hours} is invalid (must be 2-12)")
        except TypeError:
            raise InvalidPlantError("Sunlight hours must be a number!")
    
    def add_plant(self, name: str, water_level: int, sunlight_hours: int) -> None:
        if name is None or name == "":
            raise InvalidPlantError("Plant name cannot be empty!")
        
        self.validate_water_level(water_level)
        self.validate_sunlight_hours(sunlight_hours)
        
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
    
    def check_plant_health(self, plant_name: str) -> None:
        if plant_name is None or plant_name == "":
            raise InvalidPlantError("Plant name cannot be empty!")
        
        plant = None
        for p in self.plants:
            if p.name == plant_name:
                plant = p
                break
        
        if plant is None:
            raise InvalidPlantError(f"Plant '{plant_name}' not found in garden")
        
        water = plant.water_level
        sun = plant.sunlight_hours

        self.validate_water_level(water)
        self.validate_sunlight_hours(sun)
        
        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
    
    def use_water(self, amount: int) -> None:
        try:
            if amount < 0:
                raise WaterTankError("Amount cannot be negative!")
            
            if amount > self.water_tank:
                raise WaterTankError("Not enough water in tank")
        except TypeError:
            raise WaterTankError("Amount must be a number!")
        self.water_tank = self.water_tank - amount
        print(f"Used {amount} liters of water")

def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    
    garden = GardenManager()
    
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 6, 7)
        garden.add_plant("", 5, 6)
    except InvalidPlantError as error:
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
    except InvalidPlantError as error:
        print(f"Error checking lettuce: {error}")
    
    print("\nTesting error recovery...")
    try:
        garden.use_water(150)
    except WaterTankError as error:
        print(f"Caught WaterTankError: {error}")
        print("System recovered and continuing...")
    
    print("\nGarden management system test complete!")

if __name__ == "__main__":
    test_garden_management()
