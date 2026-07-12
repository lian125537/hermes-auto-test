def greet(name=""):
    if not name or not name.strip():
        name = "Guest"
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print(greet(""))
    print(greet("  "))
