# My first file tracked by Git
# Author: OSCAR CHAN
def greet(name):
 """Return a welcome message for the given name."""
 return f"Hola, {name}! Bienvenido a Git."




# This block runs only when the file is executed directly,
# not when it is imported as a module from another file.
if __name__ == "__main__":
 print(greet("Oscar")) # Call the greet function and print the result
