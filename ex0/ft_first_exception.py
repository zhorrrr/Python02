def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a number!")
        return None

    if temp < 0:
        print(f"Error: {temp}° is too cold for plants!")
        return None

    if temp > 40:
        print(f"Error: {temp}° is too hot for plants!")
        return None

    print(f"Temperature {temp}° is valid for plants!")
    return temp


def test_temperature_input() -> None:
    print("=== Testing good input ===")
    check_temperature("25")

    print("\n=== Testing bad input ===")
    check_temperature("abc")

    print("\n=== Testing extreme values ===")
    check_temperature("100")
    check_temperature("-50")

    print("\nProgram is still running!")


if __name__ == "__main__":
    test_temperature_input()
        print(f"Error: '{temp_str}' is not a number!\n")
        return None

    if temp < 0:
        print(f"Error: {temp}° is too cold for plants!\n")
        return None

    if temp > 40:
        print(f"Error: {temp}° is too hot for plants!\n")
        return None

    print(f"Temperature {temp}° is valid for plants!\n")
    return temp

def ft_first_exception() -> None:
    print("=== Garden Temperature Checker ===\n")
    temperature = ["25", "abc", "100", "-50"]
    for temp_str in temperature:
        print(f"Testing temperature: {temp_str}")
        check_temperature(temp_str)
    print("All tests completed - program didn't crash!")

   
if __name__ == "__main__":
    ft_first_exception()
