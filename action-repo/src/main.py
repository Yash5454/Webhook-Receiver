def hello_world():
    """Simple function to demonstrate the repository"""
    return "Hello, World!"

def calculate_sum(a, b):
    """Add two numbers"""
    return a + b

def calculate_product(a, b):
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    print(hello_world())
    print(f"Sum: {calculate_sum(5, 3)}")
    print(f"Product: {calculate_product(4, 6)}") 