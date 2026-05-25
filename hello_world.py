"""
My First Python Script on GitHub
Author: Aditya Raj
Role: CSDA Undergrad @ IIT Patna
"""

def generate_intro(name: str, focus_area: str) -> str:
    """Generates a professional introductory message."""
    return f"Hello, World! 🚀\nMy name is {name} and I am focusing on {focus_area}."

def main():
    # Setting up my profile details
    my_name = "Aditya Raj"
    my_interest = "Python, Data Analytics & AI"
    
    # Displaying the output beautifully
    print("=" * 50)
    print(" 🌟 WELCOME TO MY PYTHON PRACTICE REPOSITORY 🌟 ")
    print("=" * 50)
    
    print(generate_intro(my_name, my_interest))
    
    print("-" * 50)
    print("Status: Actively learning and ready to code! 💻")
    print("=" * 50)

# This is the standard way to run a Python script
if __name__ == "__main__":
    main()
