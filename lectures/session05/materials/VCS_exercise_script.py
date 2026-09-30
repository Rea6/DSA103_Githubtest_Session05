def greetings(name: str) -> str:
    """Greetings by python"""
    return f"Hello {name}!"

if __name__ == "__main__": #is only activated when main script is called, good for testing
    name = input("What is your name? ")
    print(greetings(name))