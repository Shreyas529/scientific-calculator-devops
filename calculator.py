import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def menu():
    while True:
        print("\n==== Scientific Calculator ====")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power (x^b)")
        print("5. Square (x^2)")
        print("6. Cube (x^3)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            x = float(input("Enter number: "))
            print("√{} = {}".format(x, square_root(x)))
        elif choice == '2':
            x = int(input("Enter number: "))
            print("{}! = {}".format(x, factorial(x)))
        elif choice == '3':
            x = float(input("Enter number: "))
            print("ln({}) = {}".format(x, natural_log(x)))
        elif choice == '4':
            x = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("{}^{} = {}".format(x, b, power(x, b)))
        elif choice == '5':
            x = float(input("Enter number: "))
            print("{}^2 = {}".format(x, power(x, 2)))
        elif choice == '6':
            x = float(input("Enter number: "))
            print("{}^3 = {}".format(x, power(x, 3)))
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()

