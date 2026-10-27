def add(x,y):
return x+y

def subtract(x,y):
  return x-y

def multiply(x,y);
return x*y

def divide(x,y):
  if y == 0:
    return "Error Division by zero,"
    return x / y

def calculator():
  print("Select operation:")
  print("1. Add (+)")
  print("2. Subtract (-)")
  print("3. Multiply (*)")def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y


def calculator():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input(
            "\nEnter choice (1/2/3/4) or 'q' to quit: "
        ).strip()

        if choice.lower() == "q":
            print("Calculator closed. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == "1":
                result = add(x, y)
            elif choice == "2":
                result = subtract(x, y)
            elif choice == "3":
                result = multiply(x, y)
            else:
                result = divide(x, y)

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
How to run
Copy the code into a file named calculator.py.

Open a terminal in that folder.

Run python calculator.py (or python3 calculator.py).

The calculator supports addition, subtraction, multiplication, division, invalid-input handling, division-by-zero protection, and quitting by entering q.


ChatGPT is AI and can make mistakes.
  print("4. Divide (/)")

while True:
  choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ").strip()
