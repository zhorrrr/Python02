def garden_operations(error_type : str) -> None:
    if error_type == "value":
        int("abc")
    elif error_type == "zero":
        1 / 0
    elif error_type == "file":
        open("fake_file.txt")
    elif error_type == "key":
        plants = {"rose": 5}
        print(plants["orchid"])

def test_error_types() -> None:
    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file'missing.txt'")
    
    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError:'missing_plant'")
    
    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!")
    
def ft_different_errors() -> None:
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    ft_different_errors()