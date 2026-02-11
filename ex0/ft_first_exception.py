def check_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None

    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        return None

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        return None

    print(f"Temperature {temp}°C is perfect for plants!\n")
    return temp

def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    temperature = ["25", "abc", "100", "-50"]
    for temp_str in temperature:
        print(f"Testing temperature: {temp_str}")
        check_temperature(temp_str)
    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()
