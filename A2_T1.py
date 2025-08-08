# even_or_odd.py

def check_even_odd():
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            print(f"{number} is Even.")
        else:
            print(f"{number} is Odd.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    check_even_odd()
